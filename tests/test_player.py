from escarpolette.player import Player, PlayerCommandError, State

import pytest
from unittest.mock import call


pytestmark = pytest.mark.asyncio


class TestPlayer:
    async def test_pause__playing(self, mocker):
        player = Player()
        send_command = mocker.patch("escarpolette.player.Player._send_command")

        player._state = State.PLAYING
        await player.pause()

        assert send_command.await_args_list == [call("cycle", "pause")]

    async def test_pause__paused(self, mocker):
        player = Player()
        send_command = mocker.patch("escarpolette.player.Player._send_command")

        player._state = State.PAUSED
        await player.pause()

        assert send_command.await_args_list == []

    async def test_pause__stopped(self, mocker):
        player = Player()
        send_command = mocker.patch("escarpolette.player.Player._send_command")

        player._state = State.STOPPED
        with pytest.raises(PlayerCommandError):
            await player.pause()

        assert send_command.await_args_list == []

    async def test_play__playing(self, mocker):
        player = Player()
        send_command = mocker.patch("escarpolette.player.Player._send_command")

        player._state = State.PLAYING
        await player.play()

        assert send_command.await_args_list == []

    async def test_play__paused(self, mocker):
        player = Player()
        send_command = mocker.patch("escarpolette.player.Player._send_command")

        player._state = State.PAUSED
        await player.play()

        assert send_command.await_args_list == [call("cycle", "pause")]

    async def test_play__stopped(self, mocker):
        player = Player()
        send_command = mocker.patch("escarpolette.player.Player._send_command")

        player._state = State.STOPPED
        with pytest.raises(PlayerCommandError):
            await player.play()

        assert send_command.await_args_list == []
