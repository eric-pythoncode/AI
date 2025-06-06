import nltk
import re
import heapq
from textblob import TextBlob
from colorama import Fore, Style, init
nltk.download('all')
nltk.download("punkt")
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('onw-1.4')
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

init(autoreset=True)

def summarizetext(text, summaryratio=0.3):
    sentences = sent_tokenize(text)
    words = word_tokenize(text.lower())

    stop_words = set(stopwords.words("english"))
    wordfreq = {}

    for word in words:
        if word not in stop_words and word.isalnum():
            wordfreq[word] = wordfreq.get(word, 0) + 1

    maxfreq = max(wordfreq.values(), default=1)
    for word in wordfreq:
        wordfreq[word] /= maxfreq

    sentencescores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in wordfreq:
                sentencescores[sentence] = sentencescores.get(sentence, 0) + wordfreq[word]

    summarysentences = heapq.nlargest(
        max(1, int(len(sentences) * summaryratio)), sentencescores, key=sentencescores.get
    )

    summarytext = " ".join(summarysentences)

    sentiment = TextBlob(summarytext).sentiment
    sentiment_result = f"Sentiment: {'Positive' if sentiment.polarity > 0 else 'Negative' if sentiment.polarity < 0 else 'Neutral'}"
    
    print(Fore.CYAN + Style.BRIGHT + "Summary:")
    print(Fore.YELLOW + summarytext)

    print(Fore.MAGENTA + Style.BRIGHT + sentiment_result)


text = """Artificial intelligence is transforming industries, improving efficiencies, and driving innovation.

It enables businesses to automate processes, enhance decision-making, and improve customer experience significantly.

AI-powered algorithms analyze vast amounts of data with speed and precision, allowing better insights into trends and behaviors."""

summarizetext(text, summaryratio=0.5)