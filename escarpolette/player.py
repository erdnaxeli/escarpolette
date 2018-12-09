import json
import select
import socket

from flask import current_app, _app_ctx_stack


class Player:
    """
    Control mpv using IPC.

    This is a Flask extension.
    """

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault("MPV_IPC_SOCKET", "/tmp/mpvsocket")
        app.teardown_appcontext(self.teardown)

    def teardown(self, exception):
        ctx = _app_ctx_stack.top

        if hasattr(ctx, "mpv_socket"):
            ctx.mpv_socket.close()

    @property
    def _connection(self):
        ctx = _app_ctx_stack.top
        if ctx is not None:
            if not hasattr(ctx, "mpv_socket"):
                ctx.mpv_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
                ctx.mpv_socket.connect(current_app.config["MPV_IPC_SOCKET"])

            return ctx.mpv_socket

    def _send_command(self, *args):
        """Send a command to mvp and return the response."""
        data = {"command": args}
        payload = json.dumps(data).encode("utf8") + b"\n"
        self._connection.sendall(payload)

        response = b""
        while True:
            r, _, _ = select.select([self._connection], [], [], 1)
            if r:
                response += self._connection.recv(1024)

                newline = response.find(b"\n")
                if newline >= 0:
                    # TODO
                    # find if mpv would ever return many responses
                    response = response[:newline]
                    return json.loads(response.decode("utf8"))

            else:
                # timeout
                return None

    def add_item(self, url):
        """Add a new item to the playlist."""
        self._send_command("loadfile", url, "append")

    def get_current_item_title(self):
        """Get the current playing item's title."""
        response = self._send_command("get_property", "metadata")
        return response["data"]["title"]
