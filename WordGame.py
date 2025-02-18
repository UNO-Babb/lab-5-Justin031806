#Word Game is a knock-off version of a popular online word-guessing game.

import random



def inWord(letter, word):
    """Returns boolean if letter is anywhere in the given word"""
    for ch in word:
        if letter==ch:
         return True
    return False


def inspot(letter,word,spot):
     correctLetter=word[spot]
     if letter==correctLetter:
      return True
     else:
        return False
   
def rateGuess(myGuess, word):
    """Rates your guess and returns a word with the following features.
    - Capital letter if the letter is in the right spot
    - Lower case letter if the letter is in the word but in the wrong spot
    - * if the letter is not in the word at all"""
    feedback=""

    for spot in range(5):
     myLetter = myGuess[spot]
     if inspot(myLetter,word,spot)==True:
        feedback=feedback+myLetter.upper()
     elif inWord(myLetter,word)==True:
        feedback=feedback+myLetter.lower()
     else:
          feedback=feedback+"*"

    return feedback
def main():
    #Pick a random word from the list of all words

    wordFile = open("words.txt", 'r')
    content = wordFile.read()
    wordList = content.split("\n")
    todayWord = random.choice(wordList)
    print(todayWord)

    #User should get 6 guesses to guess

    #Ask user for their guess
    ValidWord=False
    while ValidWord==False:
       
     guessNum=1
    while guessNum<=6:
     guess=input("Enter guess:")
     guess=guess.lower()
     if guess not in wordList:
        print("Word not in list.")
        validword=False
    else:
         validWord=True
    feedback=rateGuess(guess,todayWord)
    print(feedback)
    if feedback == todayWord.upper():
       print("You got it",guessNum,"tries!")
       
    guessNum=guessNum+1
    #Give feedback using on their word:
    print("The word was",todayWord)
    print("bye")





if __name__ == '__main__':
  main()
