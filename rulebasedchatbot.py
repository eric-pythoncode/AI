import re, random
from colorama import Fore, init

init(autoreset=True)

destinations = {
    "beaches": ["bali", "Maldives", "Phuket"],
    "mountains": ["Alps", "Rocky Mountains", "Himalayas"],
    "beaches": ["Tokyo", "Paris", "NYC"]
}

jokes = [
    "Why don't programmers like nature? There are too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus! ",
    "Why do travelers always feel warm? Because of all of their hot spots!"
]

def normalizeinput(text):
    print(text)
    return re.sub(r"\s+", " ", text.strip().lower())

def reccomend():
    print(Fore.CYAN + "TravelBot: Beaches, mountains, or cities?")
    preference = input(Fore.YELLOW + "You: ")
    preference = normalizeinput(preference)
    
    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(Fore.GREEN + f"TravelBot: Awesome! You could try {suggestion}!")
        print(Fore.CYAN + "Do you like it?")
        answer = input(Fore.YELLOW + "You: ".lower)
        if answer == "yes":
            print(Fore.GREEN + f"Awesome! Enjoy {suggestion}!")
        elif answer == "no":
            print(Fore.RED + f"Okay! Let's try another.")
            reccomend()
        else:
            print(Fore.RED + f"I'll try again.")
            reccomend()
    else:
        print(Fore.RED + f"Sorry, but I do not have that type of destination.")
    
    showhelp()

def packingtips():
    print(Fore.CYAN + "TravelBot: Where to?")
    location = input(Fore.YELLOW + "You: ")
    print(Fore.CYAN + "TravelBot: How many days?")    
    days = input(Fore.YELLOW + "You: " )

    print(Fore.GREEN + f"TravelBot: Packing tips for {days} days in {location}:")
    print(Fore.GREEN + f"Pack versatile clothes")
    print(Fore.GREEN + f"Bring chargers + adapters")
    print(Fore.GREEN + f"Check the weather")

def telljoke():
    print(Fore.YELLOW + f"TravelBot: {random.choice(jokes)}")

def showhelp():
    print(Fore.MAGENTA + f"\nI can:")
    print(Fore.GREEN + f"Suggest travel spots by saying 'reccomendation'")
    print(Fore.GREEN + f"Get packing tips by saying 'packing'")
    print(Fore.GREEN + f"Tell a joke by saying 'joke'")
    print(Fore.GREEN + f"End the program by typing 'exit' or 'end'")

def chat():
    print(Fore.CYAN + f"Hello! I'm TravelBot")
    name = input(Fore.YELLOW + f"Your name? ")
    print(Fore.GREEN + f"Nice to meet you, {name}")

    showhelp()

    while True:
        userinput = input(Fore.YELLOW + f"{name}: ")
        userinput = normalizeinput(userinput)
        print(userinput)
        if "reccomend" in userinput or "suggest" or "reccomendation" in userinput:
            reccomend()
        elif "pack" in userinput or "packing" in userinput:
            packingtips()
        elif "joke" in userinput or "funny" in userinput:
            telljoke()
        elif "help" in userinput:
            showhelp()
        elif "exit" in userinput or "bye" in userinput:
            print(Fore.CYAN + "Goodbye!")
            break
        else:
            print(Fore.RED + f"TravelBot: Could you please say that again?")

if __name__ == "__main__":
    chat()