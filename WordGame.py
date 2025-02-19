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
     if word[spot]==letter:
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
     
     Letter = myGuess[spot]
     if inspot(Letter,word,spot)==True:
        feedback=feedback+Letter.upper()
     elif inWord(Letter,word):
        feedback=feedback+Letter.lower()
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
    guess=input("Enter a word:")
    feedback=rateGuess(guess,todayWord)
    print(feedback)
    #Ask user for their guess
    ValidWord=False
    while ValidWord==False:
       
     guessNum=1
     feedback=""
    while guessNum<6 and feedback!=todayWord.upper():
     guess=input("Enter word:")
     feedback=rateGuess(guess,todayWord)
     print(feedback)
     guessNum=guessNum+1
     if feedback==todayWord.upper():
        print("congratulations-you got it")
     else:
        print("Sorry,the word was"+todayWord)
     
      





if __name__ == '__main__':
  main()
