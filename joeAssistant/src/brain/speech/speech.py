from playsound import playsound
from gtts import gTTS
import os


class Speech:

    def __init__(self):
        self._start_recording_sound = "startRecording.mp3"
        self._stop_recording_sound = "stopRecording.mp3"
        self._response_assistant = "response.mp3"
        self._language = "es"

    def start_recording_sound(self):
        playsound(self._start_recording_sound)

    def stopRecordingSound(self):
        playsound(self._stop_recording_sound)

    def assistant_says(self, txt):
        speechObject = gTTS(text=txt, lang=self._language, slow=False)
        speechObject.save(self._response_assistant)
        playsound(self._response_assistant)
        os.remove(self._response_assistant)
