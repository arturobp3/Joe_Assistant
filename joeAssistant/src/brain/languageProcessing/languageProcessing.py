from joeAssistant.src.brain.languageProcessing.pocketsphinxRecorder import PocketSphinxRecorder


class LanguageProcessing:

    def __init__(self):
        self.pocketsphinx_recorder = PocketSphinxRecorder()

    def listen_trigger(self):
        print("Passive listening...")
        return self.pocketsphinx_recorder.listen_trigger()