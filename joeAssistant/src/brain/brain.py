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
        '''self._memory = Memory()
        self._self_recognition = SelfRecognition()
        self._think = Think()'''

    def listen_trigger(self):
        return self._language_processing.listen_trigger()

    def run(self):
        print("run")
        while True:
            if self.listen_trigger():
                print("Trigger escuchado")
            else:
                print("Vaya, ha habido un problema")


