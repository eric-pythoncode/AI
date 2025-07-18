import queue
import sounddevice as sd
from vosk import Model, KaldiRecognizer
import pyttsx3
import json
import datetime

model = Model('C://Users//Eric//OneDrive//Desktop//Python//AI//New folder//model')
recognizer = KaldiRecognizer(model, 16000)
audioQueue = queue.Queue()
ttsEngine = pyttsx3.init()

def callback(indata, frames, time, status):
    if status:
        print(status)
    audioQueue.put(bytes(indata))

def processQuery(query):
    if "time" in query:
        now = datetime.datetime.now().strftime("%H%M")
        response = f"The current time is {now}"
    elif "date" in query:
        today = datetime.datetime.now().strftime("%B %D, %Y")
        response = f"Today is {today}"
    else:
        response = "I am sorry. Please say that again."
    return response

with sd.RawInputStream(samplerate=16000, channels=1, dtype='int16', callback=callback):
    print("Listening. . .")
    while True:
        data = audioQueue.get()
        if recognizer.AcceptWaveform(data):
            result = recognizer.Result()
            resultDict = json.loads(result)
            query = result.dict.get("text", "")
            if query:
                print("You said: ", query)
                response = processQuery(query)
                print("Response: ", response)
                ttsEngine.say(response)
                ttsEngine.runAndWait()
            else:
                print("You said nothing. Please try again.")
            
                ttsEngine.say("I'm sorry, I didn't understand that. Please try again.")
                ttsEngine.runAndWait()
