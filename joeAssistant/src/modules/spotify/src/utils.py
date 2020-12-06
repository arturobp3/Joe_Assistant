from typing import Tuple


def _get_info_from_intent(intent_request: dict, info_to_obtain: str) -> Tuple[str, None]:
    if info_to_obtain in intent_request["outcomes"][0]["entities"]:
        return intent_request["outcomes"][0]["entities"][info_to_obtain][0]["value"]
    else:
        return None


def get_elements_from_request(request: dict):
    track = _get_info_from_intent(request, "song")
    artist = _get_info_from_intent(request, "singer")
    album = _get_info_from_intent(request, "album")
    playlist = _get_info_from_intent(request, "playlist")
    return track, artist, album, playlist


def build_search_query(track=None, artist=None, album=None, playlist=None):
    query = ''
    if track is not None:
        query += track + ' '
    if artist is not None:
        query += artist + ' '
    if album is not None:
        query += 'album:' + album + ' '
    if playlist is not None:
        query += 'playlist:' + playlist + ' '
    print(query)
    return query
