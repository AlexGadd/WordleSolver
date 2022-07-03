#Importing libraries
import re
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
    re_pattern = re.compile("^" + re.escape(Chars).replace("_", ".") + "$")

    # get words that
    #   (a) are the correct length
    #   (b) aren't in the wrong guesses
    #   (c) match the pattern
    return [
        word
        for word in lst
        if (
                len(word) == len(Chars) and
                re_pattern.match(word)
        )
    ]

def LettersInPlace(Chars, lst):
    pos = 0
    for char in Chars:
        if(char.isalpha()):
            print(pos)
            print(char)
            lst = list(filter(lambda k: k.index(char) == pos, lst))
        pos += 1

#Taking inputs
GoodLetters = split(input("Please input letters that appear in the word"))
BadLetters = split(input("Please input letters that do not appear in the word"))
InPlaceChar = input("Please input letters in their respective positions, using a '-' for blank spaces")
intWordList = []
WordsLeft = []

#Filtering with good letters
WordsLeft = FilterWanted(GoodLetters, WordList)
#Filtering with bad letters
WordsLeft = FilterUnwanted(BadLetters,WordsLeft)
#Filtering with position
WordsLeft = LettersInPlace(InPlaceChar, WordsLeft)


print(f"Possible words left are {WordsLeft}")




