#Importing libraries
import urllib.request, urllib.error, urllib.parse
url = "https://static.nytimes.com/newsgraphics/2022/01/25/wordle-solver/assets/solutions.txt"

#Pulling word list
response = urllib.request.urlopen(url)
WordList = response.read().decode('UTF-8').splitlines()

#finds each occurance of a letter
def find(string, char):
    for i, c in enumerate(string):
        if c == char:
            yield i

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

#finds all letters in place
def LettersInPlace(Chars, lst):
    pos = 0
    for char in Chars:
        if(char.isalpha()):
            lst = list(x for x in lst if pos in find(x, char))
        pos += 1
    return lst

#Taking inputs
GoodLetters = split(input("Please input letters that appear in the word: "))
BadLetters = split(input("Please input letters that do not appear in the word: "))
InPlaceChar = split(input("Please input letters in their respective positions, using a '-' for blank spaces: "))
intWordList = []
WordsLeft = []

#Filtering with good letters
WordsLeft = FilterWanted(GoodLetters, WordList)
#Filtering with bad letters
WordsLeft = FilterUnwanted(BadLetters,WordsLeft)
WordsLeft = LettersInPlace(InPlaceChar, WordsLeft)


print(f"Possible words left are {WordsLeft}")




