import random 
import string
from words import hangman_words


def get_words(words):
    return random.choice(words)


def hangman():
  word= get_words(hangman_words)
  word_letters=set(word)
  alphabet=set(string.ascii_lowercase)
  used_letter=set()
  
  while len(word_letters)>0:
    print("You have used these letters"," ".join(used_letter))
    word_list=[letter if letter in used_letter else "_" for letter in word]
    print("Word to guess :"," ".join(word_list))

    user_letter=input("Enter letter: ").lower()
    if user_letter in alphabet - used_letter:
        used_letter.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter) 

    elif user_letter in used_letter:
         print("You already used that letter!")
    else:
         print("Invalid letter!")
 

hangman()