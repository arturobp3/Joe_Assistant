from pocketsphinx import get_model_path
from os import path

USERNAME = "Arturo"

FUNCTIONS = ["""Puedo interactuar con spotify y whatsapp, 
                abrir cualquier pagina web o programa del ordenador,
                buscar información en la wikipedia,
                y decirte la hora, el día y el tiempo de una ciudad que me digas. """]

KEYWORDS = ["okay joe", "joe", "okay", "though"]
EXIT_KEYWORDS = ["bye"]


MODELDIR = get_model_path()


POCKET_DICTIONARY = path.join(MODELDIR, 'cmudict-en-us.dict').replace("\\", "/")
POCKET_LANGUAGE_MODEL = path.join(MODELDIR, 'en-us.lm.bin').replace("\\", "/")
POCKET_HMM_ACOUSTIC_MODEL = path.join(MODELDIR, 'en-us').replace("\\", "/")

'''
acoustic = "C:/Users/Arturo/AppData/Local/Programs/Python/Python37/Lib/site-packages/speech_recognition/pocketsphinx-data/es-ES/acoustic-model"
lang = "C:/Users/Arturo/AppData/Local/Programs/Python/Python37/Lib/site-packages/speech_recognition/pocketsphinx-data/es-ES/language-model.lm.bin"
dicti = "C:/Users/Arturo/AppData/Local/Programs/Python/Python37/Lib/site-packages/speech_recognition/pocketsphinx-data/es-ES/pronounciation-dictionary.dict"
POCKET_DICTIONARY = dicti
POCKET_LANGUAGE_MODEL = lang
POCKET_HMM_ACOUSTIC_MODEL = acoustic'''
