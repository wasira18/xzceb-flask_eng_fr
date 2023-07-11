from deep_translator import MyMemoryTranslator

def englishToFrench(englishText):
    translator = MyMemoryTranslator(source='en-GB', target='fr-CA')
    frenchText = translator.translate(englishText)
    return frenchText

def frenchToEnglish(frenchText):
    translator = MyMemoryTranslator(source='fr-CA', target='en-GB')
    englishText = translator.translate(frenchText)
    return englishText