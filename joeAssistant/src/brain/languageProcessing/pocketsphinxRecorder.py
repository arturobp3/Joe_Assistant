from pocketsphinx import DefaultConfig, Decoder
import pyaudio
import speech_recognition as sr

from joeAssistant.src.brain.languageProcessing import config


class PocketSphinxRecorder:

    def __init__(self):
        self.conf = DefaultConfig()
        self.conf.set_string('-hmm', config.POCKET_HMM_ACOUSTIC_MODEL)
        self.conf.set_string('-lm', config.POCKET_LANGUAGE_MODEL)
        self.conf.set_string('-dict', config.POCKET_DICTIONARY)
        self.decoder = Decoder(self.conf)
        self.p_audio = pyaudio.PyAudio()
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            self.recognizer.dynamic_energy_threshold = True

    def record_trigger(self) -> bool:
        stream = self.p_audio.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
        stream.start_stream()
        self.decoder.start_utt()
        waiting = False
        wait_count = 0

        while True:
            buf = stream.read(512, exception_on_overflow=False)
            self.decoder.process_raw(buf, False, False)
            if self.decoder.hyp():
                # print("Palabra: " + self.decoder.hyp().hypstr)
                if self.decoder.hyp().hypstr in config.KEYWORDS:
                    self.decoder.end_utt()
                    return True
                else:
                    if waiting:
                        if wait_count >= 8:
                            self.decoder.end_utt()
                            return False
                        else:
                            wait_count += 1
                    else:
                        waiting = True

    # TODO: Check what happens if there's no microphone
    def record_voice_request(self) -> str:
        with self.microphone as source:
            audio = self.recognizer.listen(source, timeout=5)

        voice_request = self.recognizer.recognize_google(audio, language="es-ES")
        voice_request = voice_request.lower()
        return voice_request