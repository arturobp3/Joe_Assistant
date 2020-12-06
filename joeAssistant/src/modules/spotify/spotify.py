from typing import Tuple

from joeAssistant.src.modules.module import Module
from joeAssistant.src.modules.spotify.src import spotifyController as sc
from joeAssistant.src.modules.spotify.src.decorators import login_required

USERNAME = "arturobp"


class Spotify(Module):

    def __init__(self):
        self.spotify_controller = sc.SpotifyController()

    @login_required
    def start(self, request: dict) -> Tuple[bool, str]:
        if self.spotify_controller.start():
            return True, "Reproduciendo música de Spotify"
        else:
            return False, "Ejecuta Spotify primero"

    @login_required
    def stop(self, request: dict) -> str:
        pass

    @login_required
    def pause(self, request: dict) -> Tuple[bool, str]:  # TODO: HACER COMANDO EN WIT.AI
        self.spotify_controller.pause()
        return True, ""

    @login_required
    def update(self, request: dict) -> str:
        pass

    @login_required
    def repeat(self, request: dict) -> str:  # TODO: HACER COMANDO EN WIT.AI
        pass

    @login_required
    def next_track(self, request: dict) -> Tuple[bool, str]:
        self.spotify_controller.next_track()
        return True, ""

    @login_required
    def previous_track(self, request: dict) -> Tuple[bool, str]:
        self.spotify_controller.previous_track()
        return True, ""

    @login_required
    def turn_down_volume(self, request: dict) -> Tuple[bool, str]:
        self.spotify_controller.turn_down_volume()
        return True, ""

    @login_required
    def turn_up_volume(self, request: dict) -> Tuple[bool, str]:
        self.spotify_controller.turn_up_volume()
        return True, ""

    def currently_playing(self, request: dict):  # TODO: HACER COMANDO EN WIT.AI
        pass

    @login_required
    def play_song(self, request: dict) -> Tuple[bool, str]:  # TODO: HACER COMANDO EN WIT.AI
        success, (song, artist) = self.spotify_controller.play_song(request)
        if success:
            return True, "Reproduciendo {} de {}".format(song, artist)
        else:
            return False, "No se ha encontrado la canción {} de {}".format(song, artist)

    def play_album(self, request: dict):  # TODO: HACER COMANDO EN WIT.AI
        pass

    def play_artist(self, request: dict):  # TODO: HACER COMANDO EN WIT.AI
        pass

    def play_playlist(self, request: dict):  # TODO: HACER COMANDO EN WIT.AI
        pass

    def add_song_to_queue(self, request: dict):  # TODO: HACER COMANDO EN WIT.AI
        pass

    def activate_before_joe_speaks(self):
        self.spotify_controller.minimum_volume()

    def activate_after_joe_speaks(self):
        self.spotify_controller.restore_volume()
