from playsound import playsound
import pyaudio
from gtts import gTTS
import os


def startRecordingSound():
    playsound('..\\media\\startRecording.mp3')


def stopRecordingSound():
    playsound('..\\media\\stopRecording.mp3')


def assistantSays(text):
    speechObject = gTTS(text=text, lang="es", slow=False)
    speechObject.save("response.mp3")
    playsound('response.mp3')
    os.remove('response.mp3')


if __name__ == "__main__":
    print(os.getcwd())