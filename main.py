from guess import Guess
from replit import clear
from time import sleep
import words
import random

def main():
  playing = True
  while playing:
    game()
    sleep(1)
    print()
    playing = promptReplay()
    
def game():
  Guess.init()
  
  wordlist = words.load()
  correct = randomWord(wordlist)
  guesses = []
  win_state = False
  
  display(guesses, correct)

  while(len(guesses) < 6 and not win_state):
    guess_string = inputGuess(wordlist)
    temp = Guess(guess_string, correct)
    guesses.append(temp)
    if temp.correct:
      win_state = True
    display(guesses, correct)
  displayWin(win_state, correct)

def randomWord(wordlist):
    return wordlist[random.randrange(0, len(wordlist))]

def display(guesses, correct):
  clear()
  #print(correct)
  for guess in guesses:
    guess.display()
  for i in range(0, 6 - len(guesses)):
    print('_ _ _ _ _')
  print()
  Guess.display_letters()

def displayWin(win, correct):
  if win:
    print('GG')
  else:
    print(f'The word was {correct}.')

def inputGuess(wordlist):
  normal = '\033[0m'
  red = '\033[0;31m'
  
  guess = input('Type in word: ').lower()
  valid = Guess.verify(guess, wordlist)
  while (not valid):
    if len(guess) != 5:
      print(f'{red}Invalid length.{normal}')
    else:
      print(f'{red}Not in word bank.{normal}')
    guess = input('Type in word: ').lower()
    valid = Guess.verify(guess, wordlist)
  return guess

def promptReplay():
  inp = input('Type "y" to play again: ').lower()
  return inp == 'y'

if __name__ == "__main__":
  main()