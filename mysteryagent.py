import colorama
from colorama import Fore, Style
from textblob import TextBlob

colorama.init()

print(f"{Fore.CYAN}Welcome to the Sentiment Spy! {Style.RESET_ALL}" )

username = input(f"{Fore.MAGENTA}Please enter your name: {Style.RESET_ALL} ").strip()
if not username:
    username = "Mystery Agent"

conversationhistory = []

print(f"\n{Fore.CYAN}Hello agent {username}")
print(f"Type a sentence and I will analyze it with TextBlob and show you the sentiment")
print(f"\n{Fore.YELLOW}Type 'reset' {Fore.CYAN} to reset chats, 'history'{Fore.YELLOW} to see history, and 'exit'{Fore.YELLOW} to quit.")

while True:
    userinput = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()

    if not userinput:
        print(f"{Fore.RED}Please enter some text or a valid command.{Style.RESET_ALL}")
        continue

    elif userinput.lower() == "history":
        if not conversationhistory:
            print(f"{Fore.YELLOW}No conversation history yet.{Style.RESET_ALL}")
            for idx, (text, polarity, sentimenttype) in enumerate(conversationhistory, start=1):
                if sentimenttype == "Positive":
                    color = Fore.GREEN
                    emoji = "😀"
                elif sentimenttype == "Negative":
                    color = Fore.RED
                    emoji = "☹️"
                else:
                    sentimenttype = "Neutral"
                    color = Fore.YELLOW
                    emoji = "😐"
                
                print(f"{idx}. {color}{emoji} {text} " f"Polarity: {polarity:.2f}){Style.RESET_ALL}")
            continue

        polarity = TextBlob(userinput).sentiment.polarity
        if polarity > 0.25:
                    sentimenttype == "Positive"
                    color = Fore.GREEN
                    emoji = "😀"
        elif polarity <-0.25:
                    sentimenttype == "Negative"
                    color = Fore.RED
                    emoji = "☹️"
        else:
            color = Fore.YELLOW
            emoji = "😐"   

        conversationhistory.append((userinput, polarity, sentimenttype))

        print(f"{color}{emoji} {sentimenttype} sentiment detected!" f"Polarity: {polarity:.2f}){Style.RESET_ALL}") 
                
                
                