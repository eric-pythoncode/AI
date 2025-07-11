import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading
import speech_recognition as sr
from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

transcriptBuffer = []

recognizer = sr.Recognizer()
mic = sr.Microphone()

window = tk.Tk()
window.title("Real-time Speech Summarizer")
window.geometry('600x400')

transcriptArea = scrolledtext.ScrolledText(window, wrap=tk.WORD, height=10)
transcriptArea.pack(pady=10)

summaryArea = scrolledtext.ScrolledText(window, wrap=tk.WORD, height=10)
summaryArea.pack(pady=10)

listening = False

def listenAndTranscribe():
    global listening
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        while listening:
            try:
                audio = recognizer.listen(source, timeout=5)
                text = recognizer.recognize_google(audio)
                transcriptBuffer.append(text)
                transcriptArea.insert(tk.END, text + "\n")
            except sr.UnknownValueError:
                transcriptArea.insert(tk.END, "[Unrecognized speech.] \n")
            except sr.RequestError:
                transcriptArea.insert(tk.END, "[API unaccessable] \n")

def startListening():
    global listening
    listening = True
    threading.Thread(target=listenAndTranscribe).start()

def stopListening():
    global listening
    listening = False
    messagebox.showinfo("Stopped", "Speech recognition stopped.")

def summarizeText():
    fullText = " ".join(transcriptBuffer)
    if not fullText.strip():
        messagebox.showwarning("Empty", "No transcript to summarize")
        return
    summary = summarizer(fullText, maxLength=10, minLength=5, doSample=False)
    summaryArea.delete(1.0, tk.END)
    summaryArea.insert(tk.END, summary[0]['summary_text'])


tk.Button(window, text="Start Listening", command=startListening).pack(pady=5)
tk.Button(window, text="Stop Listening", command=stopListening).pack(pady=5)
tk.Button(window, text="Summarize", command=summarizeText).pack(pady=5)

window.mainloop()