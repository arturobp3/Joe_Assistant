"""
Facade Design Pattern:
This class provide a unified and high-level interface to the set of skills that the brain has.
"""
from joeAssistant.src.brain.languageProcessing.languageProcessing import LanguageProcessing
from joeAssistant.src.brain.selfRecognition.selfRecognition import SelfRecognition
from joeAssistant.src.brain.speech.speech import Speech
from joeAssistant.src.brain.think.think import Think

'''from joeAssistant.src.brain.memory import Memory
from joeAssistant.src.brain.think import Think'''


class Brain:

    def __init__(self):
        print("init brain")
        self._language_processing = LanguageProcessing()
        self._speech = Speech()
        self._think = Think()
        self.self_recognition = SelfRecognition()
        '''self._memory = Memory()'''

    def listen_trigger(self) -> bool:
        return self._language_processing.listen_trigger()

    def listen_voice_request(self) -> str:
        self.self_recognition.notify_joe_is_speaking()
        self._speech.start_recording_sound()
        voice_request = self._language_processing.listen_voice_request()
        self._speech.stopRecordingSound()
        self.self_recognition.notify_joe_stop_speaking()
        return voice_request

    def parse_voice_request(self, request: str) -> dict:
        return self._language_processing.parse(request)

    def execute_action(self, intent_request: dict) -> str:
        return self._think.execute_action(intent_request, self.self_recognition)
        # utilizar think o selfrecognition para saber si hay algo en marcha funcionando o si el asistente está hablando.


    def run(self):
        '''try:
            request = "pon musica"
            print(request)
            if request != "":
                info_request_dict = self.parse_voice_request(request)
                response = self.execute_action(info_request_dict)
                #print(info_request_dict)
                self._speech.say(response)
        except Exception as e:
            print(e)'''

        while True:
            if self.listen_trigger():
                print("Trigger escuchado")
                try:
                    request = self.listen_voice_request()
                    print(request)
                    if request != "":
                        info_request_dict = self.parse_voice_request(request)
                        response = self.execute_action(info_request_dict)
                        #TODO: Tener una cola de tareas que se vayan activando aquí para evitar
                        # TODO: mezclar la respuesta conla musica por ejemplo
                        self._speech.say(response)
                        print(info_request_dict)

                except Exception as e:
                    self._speech.stopRecordingSound()
                    self._speech.say(str(e))
                    self.self_recognition.notify_joe_stop_speaking()
                    print(e)
            else:
                print("Audio sin trigger")
