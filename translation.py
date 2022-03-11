#import langid # language identification (i.e. what language is this?)
# get the language id for each text
#from langid.langid import LanguageIdentifier, model
#identifier = LanguageIdentifier.from_modelstring(model, norm_probs=True)
#import dl_translate as dlt
#mt = dlt.TranslationModel()  # Slow when you load it for the first time
import torch
from easynmt import EasyNMT
modelMT = EasyNMT('opus-mt')



class TranslationServiceClient():
    def Translate_input(self, question):
        # translate french to English
        #translate_to_english = mt.translate(question, source=dlt.lang.FRENCH, target=dlt.lang.ENGLISH)
        translate_to_english = modelMT.translate(question, target_lang='en')
        return(translate_to_english)
    
    def Translate_arabic_input(self, question):
        # translate arabic to English
        translate_to_english = modelMT.translate(question, target_lang='en')
        return(translate_to_english)
    
    def Translate_output(self, answer):
        # translate english to French
        #translate_to_french = mt.translate(answer, source=dlt.lang.ENGLISH, target=dlt.lang.FRENCH)
        translate_to_french = modelMT.translate(answer, target_lang='fr')
        return(translate_to_french)
    
    def Translate_output_to_arabic(self, answer):
        # translate english to arabic
        translate_to_arabic = modelMT.translate(answer, target_lang='ar')
        return(translate_to_arabic)
    
    
    def pred_langid(self, s):
        #return identifier.classify(s)
        return modelMT.language_detection(s)

