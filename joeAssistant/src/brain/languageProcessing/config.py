from pocketsphinx import get_model_path
from os import path

KEYWORDS = ["joe", "okay", "though"]


MODELDIR = get_model_path()
POCKET_DICTIONARY = path.join(MODELDIR, 'cmudict-en-us.dict').replace("\\", "/")
POCKET_LANGUAGE_MODEL = path.join(MODELDIR, 'en-us.lm.bin').replace("\\", "/")
POCKET_HMM_ACOUSTIC_MODEL = path.join(MODELDIR, 'en-us').replace("\\", "/")

'''POCKET_DICTIONARY = path.join('C:/Users/Arturo\Desktop\JoeAssistant\joeAssistant\src/brain\languageProcessing\lang\spanish', 'es.dict').replace("\\", "/")
POCKET_LANGUAGE_MODEL = path.join('C:/Users\Arturo\Desktop\JoeAssistant\joeAssistant\src/brain\languageProcessing\lang\spanish', 'es-20k.lm').replace("\\", "/")
POCKET_HMM_ACOUSTIC_MODEL = path.join('C:/Users\Arturo\Desktop\JoeAssistant\joeAssistant\src/brain\languageProcessing\lang\spanish', 'es-es').replace("\\", "/")'''


