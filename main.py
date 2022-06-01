#Importing libraries
import urllib.request, urllib.error, urllib.parse
url = "https://static.nytimes.com/newsgraphics/2022/01/25/wordle-solver/assets/solutions.txt"

#Pulling word list
response = urllib.request.urlopen(url)
WordList = response.read().decode('UTF-8').splitlines()

#Splits strings into characters
def split(word):
    return [char for char in word]

#Keeps words with correct characters only
def FilterWanted(Chars,lst):
    for char in Chars:
        lst = list(filter(lambda k: char in k, lst))
    return lst

#removes words with incorrect characters
def FilterUnwanted(Chars,lst):
    for char in Chars:
        lst = list(filter(lambda k: char not in k, lst))
    return lst

#Taking inputs
GoodLetters = split(input("Please input letters that appear in the word"))
BadLetters = split(input("Please input letters that do not appear in the word"))
# InPlaceChar = input("Please input letters in their respective positions, using a '_' for blank spaces")
intWordList = []
WordsLeft = []

#Filtering with good letters
WordsLeft = FilterWanted(GoodLetters, WordList)
WordsLeft = FilterUnwanted(BadLetters,WordsLeft)


print(f"Possible words left are {WordsLeft}")




