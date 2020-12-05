# facade design pattern para todas las funcionalidades de spotify
from abc import ABC
from typing import Tuple

from joeAssistant.src.modules.module import Module
from joeAssistant.src.modules.spotify.src import SpotifyController as sc

USERNAME = "arturobp"


# TODO: HACER FUNCIONES CON UN DECORATOR

class Spotify(Module):

    def __init__(self):
        self.spotify_controller = sc.SpotifyController()

    def start(self) -> Tuple[bool, str]:
        if self.spotify_controller.login(USERNAME):
            if self.spotify_controller.start():
                return True, "Reproduciendo música de Spotify"
            else:
                return False, "Ejecuta Spotify primero"
        else:
            return False, "No se ha podido iniciar sesión en Spotify"

    def stop(self) -> str:
        pass

    def update(self) -> str:
        pass

    def pause(self) -> str:
        # pause_playback
        pass

    def repeat(self, mode) -> str:
        pass

    def next_track(self) -> Tuple[bool, str]:
        if self.spotify_controller.login(USERNAME):
            self.spotify_controller.next_track()
            return True, ""
        else:
            return False, "Primero ejecuta Spotify en tu ordenador"

    def previous_track(self) -> Tuple[bool, str]:
        if self.spotify_controller.login(USERNAME):
            self.spotify_controller.previous_track()
            return True, ""
        else:
            return False, "Primero ejecuta Spotify en tu ordenador"

    def turn_down_volume(self) -> Tuple[bool, str]:
        if self.spotify_controller.login(USERNAME):
            self.spotify_controller.turn_down_volume()
            return True, ""
        else:
            return False, "Primero ejecuta Spotify en tu ordenador"

    def turn_up_volume(self) -> Tuple[bool, str]:
        if self.spotify_controller.login(USERNAME):
            self.spotify_controller.turn_up_volume()
            return True, ""
        else:
            return False, "Primero ejecuta Spotify en tu ordenador"

    def minimum_volume(self):
        self.spotify_controller.minimum_volume()

    def restore_volume(self):
        self.spotify_controller.restore_volume()

    def activate_before_joe_speaks(self):
        self.minimum_volume()

    def activate_after_joe_speaks(self):
        self.restore_volume()
