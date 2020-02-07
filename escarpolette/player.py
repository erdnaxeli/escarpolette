import asyncio
import json
import logging
import select
import socket
from enum import Enum
from subprocess import Popen
from typing import Dict, Optional

from pydantic import BaseModel, ValidationError
from pydantic.fields import Field

from escarpolette.settings import Config


logger = logging.getLogger(__name__)


class MpvEvent(BaseModel):
    name: str = Field(..., alias="event")


class State(str, Enum):
    PLAYING = "PLAYING"
    PAUSED = "PAUSED"
    STOPPED = "STOPPED"


class PlayerCommandError(ValueError):
    pass


class Player:
    """Control mpv using IPC."""

    _command_id = 0
    _mpv_ipc_socket = "/tmp/mpv-socket"
    _state = State.STOPPED
    mpv: Optional[Popen] = None
    mpv_socket: Optional[socket.socket] = None

    async def init_app(self, config: Config) -> None:
        self._mpv_ipc_socket = config.MPV_IPC_SOCKET or self._mpv_ipc_socket
        self.mpv = Popen(
            [
                "mpv",
                "--idle",
                "--no-terminal",
                f"--input-ipc-server={self._mpv_ipc_socket}",
            ]
        )

        loop = asyncio.get_event_loop()
        loop.create_task(self._listen_events())

    def shutdown(self) -> None:
        if self.mpv_socket is not None:
            self.mpv_socket.close()

        if self.mpv is not None:
            # TODO: find why MPV does not respond to a SIGTERM signal
            self.mpv.kill()

    def add_item(self, url: str) -> None:
        """Add a new item to the playlist.

        If the player was stopped, play the music.
        """
        if self._state == State.STOPPED:
            self._send_command("loadfile", url, "append-play")
            self._state = State.PLAYING
        else:
            self._send_command("loadfile", url, "append")

    def get_current_item_title(self) -> Optional[str]:
        """Get the current playing item's title."""
        response = self._send_command("get_property", "metadata")
        if response is not None:
            return response["data"]["title"]

        return None

    def get_state(self) -> State:
        return self._state

    def play(self) -> None:
        """Play the current playlist."""
        if self._state == State.PLAYING:
            return
        elif self._state == State.STOPPED:
            raise PlayerCommandError("The player is stopped. Add an item to play it.")
        else:
            self._send_command("cycle", "pause")

        return None

    def pause(self) -> None:
        """Pause the current playlist."""
        if self._state == State.PAUSED:
            return
        elif self._state == State.STOPPED:
            raise PlayerCommandError("The player is stopped.")

        self._send_command("cycle", "pause")
        return None

    @property
    def _connection(self) -> socket.socket:
        if self.mpv_socket is None:
            self.mpv_socket = self._get_mpv_connection()

        return self.mpv_socket

    def _get_command_id(self) -> int:
        self._command_id += 1
        return self._command_id

    def _get_mpv_connection(self):
        mpv_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        mpv_socket.connect(self._mpv_ipc_socket)

        return mpv_socket

    async def _listen_events(self):
        """Listen for events from MVP.

        Open a connection to MVP, listen for events and update the playlist
        accordingly.
        """
        # We want to let MPV start
        await asyncio.sleep(2)

        logger.info("Connecting to MVP on %s", self._mpv_ipc_socket)
        reader, _ = await asyncio.open_unix_connection(self._mpv_ipc_socket)
        logger.info("Connected to MVP")

        while True:
            data = await reader.readuntil(b"\n")
            logger.debug("Received event from MVP: %s", data)

            try:
                event_data = json.loads(data)
            except json.JSONDecodeError as e:
                logger.debug("Cannot decode MVP event: %s", e)

            try:
                event = MpvEvent(**event_data)
            except ValidationError as e:
                logger.debug("Received unknown data from MPV: %s", e)
                continue

            if event.name == "idle":
                logger.info("Player stopped")
                self._state = State.STOPPED
            elif event.name == "pause":
                logger.info("Player paused")
                self._state = State.PAUSED
            elif event.name == "start-file":
                logger.info("Player playing")
                self._state = State.PLAYING
            elif event.name == "unpause":
                logger.info("Player playing")
                self._state = State.PLAYING
            else:
                logger.debug("Unknow MPV event %s", event.name)

    def _send_command(self, *command: str) -> Optional[Dict]:
        """Send a command to MPV and return the response."""
        command_id = self._get_command_id()
        msg = {"command": command, "request_id": command_id}
        logger.debug("Sending MPV command %s", msg)

        data = json.dumps(msg).encode("utf8") + b"\n"
        self._connection.sendall(data)

        return self._read_response(command_id)

    def _read_response(self, command_id: int) -> Optional[Dict]:
        data = b""
        while True:
            r, _, _ = select.select([self._connection], [], [], 1)
            if not r:
                # timeout
                return None

            data += self._connection.recv(1024)

            newline = data.find(b"\n")
            if newline == -1:
                next

            response = data[:newline]
            data = data[newline:]

            msg = json.loads(response.decode("utf8"))
            logger.debug("Received MPV response %s", msg)
            if msg.get("request_id", -1) == command_id:
                return msg


_current_player = Player()


def get_player():
    return _current_player
