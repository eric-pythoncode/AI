import speech_recognition as sr
import pyttsx3
from datetime import datetime
from playsound import playsound
import random

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

def getAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now. . .")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Could not understand.")
        except sr.RequestError as e:
            print(f"API error: {e}")
        return ""
    
jokes = [

"Why did the computer go to therapy? Because it had too many issues.",

"Why do programmers prefer dark mode? Because the light attracts bugs!",

"How did the JavaScript developer fix the broken keyboard? By checking the event logs.",

"Why did Python break up with Java? Because it had too many class issues!",

"What do you call a group of musical coders? A code band!"

]

def respondToCommand(command):
    if "hello" in command:
        speak("Hello! How can i help you?")
    elif "your name" in command:
        speak("I am your AI assistant")
    elif "date" in command:
        speak(datetime.now().strftime("Today is %A, %d, %B %Y"))
    elif "play music" in command:
        speak("Playing music")
        try:
            playsound("song.mp3")
        except Exception as e:
            print(f"Sorry, there was an error in playing the song: {e}")
    elif "joke" in command:
        joke = random.choice(jokes)
        speak(joke)
    elif "stop" or "quit" or "exit" in command:
        speak("Goodbye!")
        return False
    else:
        speak("Sorry, I did not understand that.")
    return True

if __name__ == "__main__":
    speak("Voice assistant activated!")
    running = True
    while running:
        command = getAudio()
        if command:
            running = respondToCommand(command)
