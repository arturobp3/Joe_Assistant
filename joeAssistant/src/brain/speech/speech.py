from playsound import playsound
import pyttsx3


class Speech:

    def __init__(self):
        self._start_recording_sound = '..\\assets\\startRecording.mp3'
        self._stop_recording_sound = '..\\assets\\stopRecording.mp3'
        self._engine = pyttsx3.init()
        self._engine.setProperty('rate', 120)
        self._engine.setProperty('volume', 1)

    def start_recording_sound(self):
        playsound(self._start_recording_sound)

    def stopRecordingSound(self):
        playsound(self._stop_recording_sound)

    def say(self, text):
        self._engine.say(text)
        self._engine.runAndWait()
