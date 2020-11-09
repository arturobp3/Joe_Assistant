"""
Facade Design Pattern:
This class provide a unified and high-level interface to the set of skills that the brain has.
"""
from joeAssistant.src.brain.languageProcessing.languageProcessing import LanguageProcessing
from joeAssistant.src.brain.speech.speech import Speech

'''from joeAssistant.src.brain.memory import Memory
from joeAssistant.src.brain.selfRecognition import SelfRecognition
from joeAssistant.src.brain.think import Think'''


class Brain:

    def __init__(self):
        print("init brain")
        self._language_processing = LanguageProcessing()
        self._speech = Speech()
        # self._think = Think()
        '''self._memory = Memory()
        self._self_recognition = SelfRecognition()'''

    def listen_trigger(self) -> bool:
        return self._language_processing.listen_trigger()

    def listen_voice_request(self) -> str:
        return self._language_processing.listen_voice_request()

    def parse_voice_request(self, request: str) -> dict:
        return self._language_processing.parse(request)

    def run(self):
        while True:
            if self.listen_trigger():

                print("Trigger escuchado")

                self._speech.start_recording_sound()
                try:
                    request = self.listen_voice_request()
                    self._speech.stopRecordingSound()
                    print(request)
                    if request != "":
                        info_request_dict = self.parse_voice_request(request)
                        #response = self.execute_action(info_request_dict)
                        #self._speech.say(response)
                        print(info_request_dict)

                except Exception as e:
                    self._speech.stopRecordingSound()
                    self._speech.say(str(e))
            else:
                print("Audio sin trigger")
