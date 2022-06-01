import urllib.request, urllib.error, urllib.parse
url = "https://static.nytimes.com/newsgraphics/2022/01/25/wordle-solver/assets/solutions.txt"

response = urllib.request.urlopen(url)
WordList = response.read().decode('UTF-8').splitlines()

GoodLetters = input("Please input letters that appear in the word")
# BadLetters = input("Please input letters that do not appear in the word")
# InPlaceChar = input("Please input letters in their respective positions, using a '_' for blank spaces")
intWordList = []
WordsLeft = []

for word in WordList:
    for char in GoodLetters:
        if char in word:
            intWordList.append(word)

print(f"Possible words left are {WordsLeft}")



# list(filter(lambda k: 'ab' in k, lst))
