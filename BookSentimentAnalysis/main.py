import re
import nltk
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('stopwords')
nltk.download('vader_lexicon')

# Loading the book
with open("miracle_in_the_andes.txt", 'r', encoding="utf8") as fh:
    book = fh.read()

# The most used words (non-articles)
pattern = re.compile("[a-zA-Z]+")
findings = re.findall(pattern, book.lower())

# Count the words
word_dict = {}
for word in findings:
    if word not in word_dict.keys():
        word_dict[word] = 1
    else:
        word_dict[word] = word_dict[word] + 1

# Make a list and sort the words
word_list = [(value, key) for (key, value) in word_dict.items()]
word_sorted = sorted(word_list, reverse=True)
print(word_sorted)

# Get English stop words
eng_stopwords = stopwords.words("english")

# Get the filtered words
filtered_words = []
for count, word in word_sorted:
    if word not in eng_stopwords:
        filtered_words.append((word, count))

print(filtered_words)

# Sentiment Analysis: What is the most positive and the most negative chapter?
analyzer = SentimentIntensityAnalyzer()
analysis = analyzer.polarity_scores(book)
print(analysis)

if analysis["pos"] > analysis["neg"]:
    print("It is a positive text")
else:
    print("It is a negative text")

# Chapter sentiment analysis
pattern = re.compile("Chapter [0-9a-zA-Z]+")
chapters = re.split(pattern, book)
chapters = chapters[1:]

for nr, chapter in enumerate(chapters):
    analysis = analyzer.polarity_scores(chapter)

    if analysis["pos"] > analysis["neg"]:
        print(f"{nr + 1}. It is a positive text")
    else:
        print(f"{nr + 1}. It is a negative text")


"""

# How many chapters?
pattern = re.compile("Chapter [0-9]+")
chapters = re.findall(pattern, book)
n_chapters = len(chapters)
print(n_chapters)

# How many chapters?
pattern = re.compile("Chapter [a-zA-Z]+")
chapters = re.findall(pattern, book)
n_chapters = len(chapters)
print(n_chapters)

# Which are the sentences where "love" was used?
pattern = re.compile("[A-Z]{1}[^.]*[^a-zA-Z]+an[^a-zA-Z]+[^.]*.")
findings = re.findall(pattern, book)
print(findings)

# What are the most used words?
pattern = re.compile("[a-zA-Z]+")
findings = re.findall(pattern, book.lower())
print(findings)
print(len(findings))

# Count the words
word_dict = {}
for word in findings:
    if word not in word_dict.keys():
        word_dict[word] = 1
    else:
        word_dict[word] = word_dict[word] + 1

# Make a list and sort the words
word_list = [(value, key) for (key, value) in word_dict.items()]
word_sorted = sorted(word_list, reverse=True)
print(word_sorted)

# Extract the paragraph where "an" was used
pattern = re.compile("[^\n]+an[^\n]+")
findings = re.findall(pattern, book)
print(findings)

# Extract the chapter titles
pattern = re.compile("[a-zA-Z ,]+\n\n")
findings = re.findall(pattern, book)
findings =[item.strip("\n\n") for item in findings]
print(findings)

pattern = re.compile("([a-zA-Z ]+)\n\n")
findings = re.findall(pattern, book)
print(findings)

# Function that finds the occurrence of any word
def find(w):
    pattern = re.compile("[a-zA-Z]+")
    findings = re.findall(pattern, book.lower())

    # Count the words
    word_dict = {}
    for word in findings:
        if word not in word_dict.keys():
            word_dict[word] = 1
        else:
            word_dict[word] = word_dict[word] + 1

    try:
        return word_dict[w]
    except:
        return f"The book does not contain the word '{w}'"

print(find("love"))
print(find("the"))

"""