from escarpolette.player import Player, PlayerCommandError, State

import pytest
from unittest.mock import call


class TestPlayer:
    def test_pause__playing(self, mocker):
        player = Player()
        send_command = mocker.patch("escarpolette.player.Player._send_command")

        player._state = State.PLAYING
        player.pause()

        assert player._state == State.PAUSED
        assert send_command.mock_calls == [call("cycle", "pause")]

    def test_pause__paused(self, mocker):
        player = Player()
        send_command = mocker.patch("escarpolette.player.Player._send_command")

        player._state = State.PAUSED
        player.pause()

        assert player._state == State.PAUSED
        assert send_command.mock_calls == []

    def test_pause__stopped(self, mocker):
        player = Player()
        send_command = mocker.patch("escarpolette.player.Player._send_command")

        player._state = State.STOPPED
        with pytest.raises(PlayerCommandError):
            player.pause()

        assert player._state == State.STOPPED
        assert send_command.mock_calls == []

    def test_play__playing(self, mocker):
        player = Player()
        send_command = mocker.patch("escarpolette.player.Player._send_command")

        player._state = State.PLAYING
        player.play()

        assert player._state == State.PLAYING
        assert send_command.mock_calls == []

    def test_play__paused(self, mocker):
        player = Player()
        send_command = mocker.patch("escarpolette.player.Player._send_command")

        player._state = State.PAUSED
        player.play()

        assert player._state == State.PLAYING
        assert send_command.mock_calls == [call("cycle", "pause")]

    def test_play__stopped(self, mocker):
        player = Player()
        send_command = mocker.patch("escarpolette.player.Player._send_command")

        player._state = State.STOPPED
        with pytest.raises(PlayerCommandError):
            player.play()

        assert player._state == State.STOPPED
        assert send_command.mock_calls == []
