import requests
import tkinter as tk
from tkinter import messagebox, scrolledtext

categories = {
    "Random": "https://uselessfacts.jsph.pl/random.json?language=en",
    "Technology": "https://uselessfacts.jsph.pl/random.json?language=en",
    "Science": "https://uselessfacts.jsph.pl/random.json?language=en"
}

def getfact():
    selectedcategory = categoryvar.get()
    url = categories[selectedcategory]

    try:
        response = requests.get(url)
        response.raise_for_status()

        factdata = response.json()
        fact = factdata.get('text', "No Fact Found!")
        
        outputbox.delete('1.0', tk.END)
        outputbox.insert(tk.END, f"{selectedcategory} fact:\n{fact}")

        if savevar.get():
            with open("saved_facts.txt", "a") as file:
                file.write(f"{selectedcategory}: {fact}\n")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error: ", f"Failed to fetch fact: {e}")

root = tk.Tk()
root.title("Fact Finder")
root.geometry("500x300")
root.resizable(False, False)

heading = tk.Label(root, text="Random Facts", font=("Arial", 14, "bold"))
heading.pack(pady=10)

categoryvar = tk.StringVar(root)
categoryvar.set("Random")
categorymenu = tk.OptionMenu(root, categoryvar, *categories.keys())
categorymenu.pack()

outputbox = scrolledtext.ScrolledText(root, width=60, height=10, font=("Arial", 10))
outputbox.pack(pady=10)

savevar = tk.BooleanVar()
savecheckbox = tk.Checkbutton(root, text="Save fact to file", variable=savevar)
savecheckbox.pack()

fetchbutton = tk.Button(root, text="Get Fact", command=getfact, bg="blue", fg="white", font=("Arial", 12))
fetchbutton.pack(pady=10)

exitbutton = tk.Button(root, text="Exit", command=root.destroy, bg="red", fg="white", font=("Arial", 10))
exitbutton.pack(pady=5)

root.mainloop()
