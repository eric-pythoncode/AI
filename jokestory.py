import requests
import tkinter as tk
from tkinter import messagebox
import random
import pyttsx3

engine = pyttsx3.init()

stories = [
"Once upon a time, a tiny turtle wanted to fly. He flapped his arms and jumped. He didn’t fly, but he made his friends laugh!",
"A clever fox once tricked a proud lion into dancing in front of the forest. The animals never forgot the day the lion danced!",
]

poems = [
"Roses are red,\nViolets are blue,\nCoding is fun,\nEspecially with you!",
"In the garden of code I grow,\nWith loops and logic, I gently flow.",
]

def speak(text):
    engine.say(text)
    engine.runAndWait()

def getjoke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)

    if response.status_code == 200:
        joke = response.json()
        joketext = f"{joke['setup']} ... {joke['punchline']}!"
        output.set(joketext)
        speak(joketext)
    else:
        print("Failed to fetch joke!")

    
def showstory():
    story = random.choice(stories)
    output.set(story)
    speak(story)

def showpoem():
    poem = random.choice(poems)
    output.set(poem)
    speak(poem)

root = tk.Tk()
root.title("Fun Reader")
root.geometry("500x450")
root.configure(bg='lavender')

output = tk.StringVar()
label = tk.Label(root, textvariable=output, wraplength=450, justify='center', font=('Arial', 12), bg='lavender')
label.pack(pady=30)

btnjoke = tk.Button(root, text="Tell a Joke", command=getjoke, font=('Arial', 12), bg='lightblue')
btnjoke.pack(pady=5)

btnstory = tk.Button(root, text="Read a Story", command=showstory, font=('Arial', 12), bg='lightgreen')
btnstory.pack(pady=5)

btnpoem = tk.Button(root, text="Read a Poem", command=showpoem, font=('Arial', 12), bg='lightpink')
btnpoem.pack(pady=5)

root.mainloop()