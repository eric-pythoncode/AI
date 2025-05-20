import requests
import tkinter as tk
from tkinter import messagebox

def getjoke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)

    if response.status_code == 200:
        joke = response.json()
        setup = joke['setup']
        punchline = joke['punchline']
        joketext.set(f"{setup}\n\n{punchline}")
    else:
        print("Failed to fetch joke!")

root = tk.Tk()
root.title("Random Joke Generator")
root.geometry("400x300")
root.configure(bg='lightyellow')

joketext = tk.StringVar()
jokelabel = tk.Label(root, textvariable=joketext, wraplength=150, justify='center', font=("Arial", 12),bg='lightyellow')
jokelabel.pack(pady=40)

jokebutton = tk.Button(root, text="Tell me a joke", command=getjoke, font=("Arial", 14), bg='lightblue')
jokebutton.pack(pady=20)
root.mainloop()