import struct
from pocketsphinx import DefaultConfig, Decoder
import speech_recognition as sr
import outputSounds as out
import pyaudio
import setup
import audioop
import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import noisereduce as nr
from scripts.skills import skillsController as sc
from adaptfilt import nlms as nl
from adaptfilt import misc as mi
from scipy.io import wavfile
import winsound

TRIGGER_WORD = "success"
CANCEL = "bye"
KEYWORDS = ["ok jerry", "okay terry", "okay denny"]
DTYPE = np.int16


class AudioRecorder:

    def __init__(self):
        # Create a decoder with certain model
        self.conf = DefaultConfig()
        self.conf.set_string('-hmm', setup.POCKET_HMM_ACOUSTIC_MODEL)
        self.conf.set_string('-lm', setup.POCKET_LANGUAGE_MODEL)
        self.conf.set_string('-dict', setup.POCKET_DICTIONARY)
        # self.conf.set_string('-remove_noise', 'yes')

        # Decode streaming data
        self.decoder = Decoder(self.conf)
        self.p_audio = pyaudio.PyAudio()
        self.skillsController = sc.SkillsController()

        # Set up speech recognition recognizer and microphone
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            self.recognizer.dynamic_energy_threshold = True

    def listen_keyword(self):
        """
        Passively listens until some trigger word is heard
        Return the type of trigger heard
        """
        stream = self.p_audio.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
        stream.start_stream()

        print("Passive listening...")
        # Process audio chunk by chunk. On keyword detected, perform action and restart search
        self.decoder.start_utt()
        waiting = False
        wait_count = 0

        while True:
            buf = stream.read(256, exception_on_overflow=False)

            '''rms = audioop.rms(buf, 2)
            decibel.append(20 * math.log10(rms))
            #if 20 * math.log10(rms) >= 77:'''

            self.decoder.process_raw(buf, False, False)
            # Check whether a hypothesis was formed
            if self.decoder.hyp():
                print("Palabra: " + self.decoder.hyp().hypstr)

                # Check whether trigger word was heard
                if self.decoder.hyp().hypstr in setup.KEYWORDS:
                    self.decoder.end_utt()
                    return TRIGGER_WORD
                elif self.decoder.hyp().hypstr in setup.EXIT_KEYWORDS:
                    self.decoder.end_utt()
                    return CANCEL
                else:
                    if waiting:
                        if wait_count >= 8:
                            self.decoder.end_utt()
                            return "failed"
                        else:
                            wait_count += 1
                    else:
                        waiting = True

    def recordVoiceCommand(self):
        """
         Actively listens what the user is saying
         Return what the user has said in a String format
         """
        with self.microphone as source:
            audio = self.recognizer.listen(source, timeout=5)

        data = ''
        try:
            data = self.recognizer.recognize_google(audio, language="es-ES")
            data = data.lower()

        except sr.UnknownValueError as e:
            print(e)
            return -1

        except sr.RequestError as e:
            print(e)
            return -2

        except sr.WaitTimeoutError as e:
            print(e)
            return data

        except:
            return -3

        finally:
            return data

    def runRecorder(self):
        # Start passive listener and, when a trigger word is heard, start active listener
        while True:
            trigger = self.listen_keyword()
            if trigger == TRIGGER_WORD:
                out.startRecordingSound()
                userSays = self.recordVoiceCommand()
                out.stopRecordingSound()

                if userSays == -1:  # The assistant didn't understand what I've said
                    out.assistantSays("No he podido entenderte, repítemelo otra vez.")

                elif userSays == -2:  # The assistant is not made to do that task
                    out.assistantSays("No estoy hecho para hacer esa tarea.")

                elif userSays == -3:  # Something weird happened
                    out.assistantSays("Algo raro ha pasado")

                elif userSays == "":
                    continue

                else:
                    #out.assistantSays(userSays)
                    self.skillsController.analyseCommand(userSays)

            elif trigger == CANCEL:
                break

        out.assistantSays("Adios")


if __name__ == '__main__':
    recorder = AudioRecorder()
    recorder.runRecorder()
