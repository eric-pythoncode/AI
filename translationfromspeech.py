import speech_recognition as sr
import pyttsx3
from googletrans import Translator

def speak(text, language='en'):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')

    if language == 'en':
        engine.setProperty('voice', voices[0].id)
    else:
        engine.setProperty('voice', voices[1].id)

    engine.say(text)
    engine.runAndWait()

def speechToText():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak now in English")
        audio = recognizer.listen(source)

    try:
        print("Recognizing speech.")
        text = recognizer.recognize_google(audio, language='en-US')
        print(f"You said {text}")
    except sr.UnknownValueError:
        print("Could not understand the audio") 
    except sr.RequestError as e:
        print(f"Error getting API: {e}")
    return ""

def translateText(text, target_language="es"):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    print(f"Translated text: {translation.text}")
    return translation.text

def displayLanguageOptions():
        choice = input("Please select the target language number (1-8) ")
        languageDict = {
        "1": "hi",
        "2": "ta",
        "3": "te",
        "4": "bn",
        "5": "mr",
        "6": "gu",
        "7": "mi",
        "8": "pa"

        } 

        return languageDict.get(choice, "es")

def main():
    targetLanguage = displayLanguageOptions()

    originalText = speechToText()

    if originalText:
        translatedText = translateText(originalText, target_language=targetLanguage)

        speak(translatedText, language='en')
        print("Translated text spoken")

if __name__ == "__main__":
    main()