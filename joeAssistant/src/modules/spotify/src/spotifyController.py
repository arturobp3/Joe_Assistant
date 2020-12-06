from json import JSONDecodeError
import json
from typing import Tuple, Any

import spotipy
import spotipy.util as util
from webbot import Browser
import os
import time


import joeAssistant.src.auth_credentials as credentials
import joeAssistant.src.modules.spotify.src.utils as spotify_utils


USERNAME = "arturobp"


class SpotifyController:

    def __init__(self):
        self.token = None
        self.spotipy = None
        self.active_device = None
        self.loginDone = False
        self.volume_percent = None

    def login(self, username) -> bool:
        try:
            self.token = util.prompt_for_user_token(username, scope=credentials.SPOTIPY_SCOPES,
                        client_id=credentials.SPOTIPY_CLIENT_ID,
                        client_secret=credentials.SPOTIPY_CLIENT_SECRET,
                        redirect_uri=credentials.SPOTIPY_REDIRECT_URI)
            self.spotipy = spotipy.Spotify(auth=self.token)
            print(self.spotipy.devices())
            self.active_device = self.spotipy.devices()["devices"][0]["id"]
            self.volume_percent = self.spotipy.devices()["devices"][0]["volume_percent"]
            self.loginDone = True
            return True
        except Exception as e:
            print(e)
            self.loginDone = False
            return False

    def start(self) -> bool:
        try:
            self.spotipy.transfer_playback(device_id=self.active_device, force_play=True)
            return True
        except Exception as e:
            print(e)
            return False

    def next_track(self):
        self.spotipy.next_track(self.active_device)

    def previous_track(self):
        self.spotipy.previous_track(self.active_device)

    def pause(self):
        self.spotipy.pause(self.active_device)

    def turn_down_volume(self):
        self.volume_percent = self.spotipy.devices()["devices"][0]["volume_percent"]
        self.spotipy.volume(self.volume_percent - 25, self.active_device)
        self.volume_percent = self.volume_percent - 25

    def turn_up_volume(self):
        self.volume_percent = self.spotipy.devices()["devices"][0]["volume_percent"]
        self.spotipy.volume(self.volume_percent + 25, self.active_device)
        self.volume_percent = self.volume_percent + 25

    def minimum_volume(self):
        if len(self.spotipy.devices()["devices"]) > 0:
            self.volume_percent = self.spotipy.devices()["devices"][0]["volume_percent"]
            self.spotipy.volume(20, self.active_device)

    def restore_volume(self):
        if len(self.spotipy.devices()["devices"]) > 0:
            self.spotipy.volume(self.volume_percent, self.active_device)

    def play_song(self, request: dict) -> Tuple[bool, Tuple[Any, Any]]:
        song, artist, album, playlist = spotify_utils.get_elements_from_request(request)
        search_query = spotify_utils.build_search_query(track=song, artist=artist, album=album, playlist=playlist)
        result = self.spotipy.search(q=search_query, type='track')
        print("Resultado busqueda: " + str(result))
        if result["tracks"]["total"] > 0:
            artist_name = result["tracks"]["items"][0]["artists"][0]["name"]
            song_name = result["tracks"]["items"][0]["name"]
            uri = result["tracks"]["items"][0]["uri"]
            self.spotipy.start_playback(device_id=self.active_device, uris=[uri])
            return True, (song_name, artist_name)
        else:
            return False, (song, artist)



