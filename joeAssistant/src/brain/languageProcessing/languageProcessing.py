import speech_recognition as sr
from wit import Wit

from joeAssistant.src import auth_credentials as auth
from joeAssistant.src.brain.languageProcessing.pocketsphinxRecorder import PocketSphinxRecorder
from joeAssistant.src.brain.languageProcessing.exceptions.exceptions import NoRequestHeardError, \
    LanguageProcessingGeneralError, UnintelligibleRequestError


class LanguageProcessing:

    def __init__(self):
        self._pocketsphinx_recorder = PocketSphinxRecorder()
        self._wit_client = Wit(auth.WIT_SERVER_ACCESS_TOKEN)

    def listen_trigger(self) -> bool:
        print("Passive listening...")
        return self._pocketsphinx_recorder.record_trigger()

    def listen_voice_request(self) -> str:
        voice_request = ""
        try:
            voice_request = self._pocketsphinx_recorder.record_voice_request()
        except sr.WaitTimeoutError:
            print("No request heard")
            raise NoRequestHeardError("")
        except sr.UnknownValueError:
            print("language processing general error")
            raise LanguageProcessingGeneralError("Perdona, no he podido entender lo que has dicho.")
        except sr.RequestError:
            print("peticion no se entiende")
            raise UnintelligibleRequestError("Actualmente no puedo hacer eso.")

        return voice_request

    def parse(self, request: str) -> dict:
        return self._wit_client.get_message(request)


