import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob
from colorama import init, Fore
import time
import sys

init(autoreset=True)

def loaddata(file_path="imdb_top_1000.csv"):
    try:
        df = pd.read_csv(file_path)
        df['combined features'] = df['Genre'].fillna('') + ' ' + df['Overview'].fillna('')
        return df
    except FileNotFoundError:
        print(Fore.RED + f"Error: The file {file_path} has not been found")
        exit()

movies_df = loaddata()
print(movies_df)
tfidf = TfidfVectorizer(stop_words='english')
tfidfmatrix = tfidf.fit_transform(movies_df['combined features'])
cosinesim = cosine_similarity(tfidfmatrix, tfidfmatrix)

def listgenres(df):
    return sorted(set(genre.strip() for sublist in df['Genre'].dropna().str.split(',') for genre in sublist))

genres = listgenres(movies_df)
def reccomendmovies(genre=None, mood=None, rating=None, topn=5):
    filtereddf = movies_df
    if genre:
        filtereddf = filtereddf[filtereddf['Genre'].str.contains(genre, case=False, na=False)]
    if rating:
        filtereddf = filtereddf[filtereddf['IMDB Rating'] >= rating]

    filtereddf = filtereddf.sample(frac=1).reset_index(drop=True)

    reccomendations = []
    for idx, row in filtereddf.iterrows():
        overview = row['Overview']
        if pd.isna('Overview'):
            continue
        polarity = TextBlob(overview).sentiment.polarity
        if (mood and ((TextBlob(mood).sentiment.polarity < 0 and polarity > 0) or polarity >= 0)) or not mood:
            reccomendations.append((row['Series Title'], polarity))
        if len(reccomendations) == topn:
            break

    return reccomendations if reccomendations else "No suitable movies found"

def displayreccomendations(recs, name):
    print(Fore.YELLOW + f"'\nAI Analyzed Movie Reccomendations for {name}:")
    for idx, (title, polarity) in enumerate(recs, 1):
        sentiment = "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"
        print(f"{Fore.CYAN}{idx}. {title} - Polarity: {polarity:.2f}, {sentiment}")

def processinganimation():
    for _ in range(3):
        print(Fore.YELLOW + ".", end="", flush=True)
        time.sleep(0.5)

def handleai(name):
    print(Fore.BLUE + "\nLet's find the perfect movie for you!")


    print(Fore.GREEN + "Available genres: ", end="")
    for idx, genre in enumerate(genres, 1):
        print(f"{Fore.CYAN}{idx}. {genre}")
    print()


    while True:
        genreinput = input(Fore.YELLOW + "Enter your genre number or name: ").strip()
        if genreinput.isdigit() and 1 <= int(genreinput) <= len(genres):
            genre = genres[int(genreinput)-1]
            break
        elif genreinput.title() in genres:
            genre = genreinput.title()
            break
        print(Fore.RED + "Invalid input. Try again. \n")

    mood = input(Fore.YELLOW + "How do you feel today? Describe your mood:").strip()
    print(Fore.BLUE + "\nAnalyzing mood", end="", flush=True )
    processinganimation()
    polarity = TextBlob(mood).sentiment.polarity
    mooddesc = "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"
    print(f"\n{Fore.GREEN}Your mood is {mooddesc} (Polarity: {polarity:.2f}).\n")

    while True:
        ratinginput = input(Fore.YELLOW + "Enter minimum IMDB rating (7.6 - 9.3) or 'skip").strip()
        if ratinginput.lower() == "skip":
            rating = None
            break
        try:
            rating = float(ratinginput)
            if 7.6 <= rating <= 9.3:
                break
            print(Fore.RED + "Rating out of range. Try again.\n")
        except ValueError:
            print(Fore.RED + "Invalid input. Try again.\n")


    print(f"Finding movies for {name}", end="", flush=True)
    processinganimation()

    recs = reccomendmovies(genre=genre, mood=mood, rating=rating, topn=5)
    if isinstance(recs, str):
        print(Fore.RED + recs + "\n")
    else:
        displayreccomendations(recs, name)

    while True:
        action = input(Fore.YELLOW + "\nWould you like more reccomendations? yes or no:").strip().lower()
        if action == 'no':
            print(Fore.GREEN + f"Enjoy your movie picks, {name}!")
            break
        elif action == "yes":
            recs = reccomendmovies(genre=genre, mood=mood, rating=rating, topn=5)
            if isinstance(recs, str):
                print(Fore.RED + recs + "\n")
            else:
                displayreccomendations(recs, name)
        else:
            print(Fore.RED + "Invalid choice. Try again. \n")


def main():
    print(Fore.BLUE + "Welcome to the Personal Movie Reccomendation Assistant!")
    name = input("What is your name? ").strip()
    print(f"\n{Fore.GREEN}Great to meet you, {name}! \n")
    handleai(name)

if __name__ == "__main__":
    main()