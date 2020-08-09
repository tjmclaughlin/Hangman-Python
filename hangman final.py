#Hangman Python Game
#Thomas McLaughlin
#8-1-2020

import random
from nltk.corpus import words

#method to split word
def split(word):
    return [char for char in word]

#method to display secret_word guessing progress
def display(right_guesses, secret_word_chars):
    for i in range(len(secret_word_chars)):
        if secret_word_chars[i] in right_guesses:
            print(secret_word_chars[i] + " ", end="")
        else:
            print("_ ", end="")
    print("\n")

#generate random word from list
word_list = words.words()
random_int = random.randint(1, len(word_list))
secret_word = word_list[random_int].lower()

#store characters of secret_word in secret_word_list
secret_word_chars = split(secret_word)
secret_word_list = split(secret_word)

#set lives_remaining to 6, wrong guesses list created, guessed status = False
lives_remaining = 6
wrong_guesses = []
right_guesses = []
guessed = False

#tell user amount characters of secret_word
print("Amount of characters of secret word: " + str(len(secret_word_list)))


while guessed == False:
    #inform user of how many characters there is, and how many lives remaing
    print("You have " + str(lives_remaining) + " live(s) remaining.")

    #ask user for character or word input
    user_input = input("Guess a character or word: ").lower()
    #if input is guessed, inform them to try again
    if user_input in right_guesses or user_input in wrong_guesses:
        print("Already guessed, try again")
    else:
        #if input is correct, lives_remaining is unchanged, that letter is filled in from where found in secret_word_list
        if len(user_input) == 1:
            if user_input in secret_word_list:
                print("Correct guess, found character " + user_input + " in: " + str(secret_word_list.count(user_input)) + " appearance(s).")
                while user_input in secret_word_list: #deals with duplicates
                    right_guesses.append(user_input)
                    secret_word_list.remove(user_input)
        #if input is incorrect, lives_remaining - 1, and that letter is added to incorrect guesses
            else:
                print("incorrect")
                lives_remaining -= 1
                wrong_guesses.append(user_input)
        else:
            if user_input == secret_word:
                guessed = True
            else:
                print("WRONG!")
                lives_remaining -= 1
        #if all letters guessed, game wins
        if len(secret_word_list) == 0 and lives_remaining > 0:
            guessed = True
        #if no lives remain, game over
        if lives_remaining == 0:
            print("SORRY, YOU LOSE. THE WORD WAS: " + secret_word.upper() + ", PLEASE TRY AGAIN!")
            break
        #display secret_word guessing progress after recent update
        if len(user_input) == 1:
            display(right_guesses, secret_word_chars)

#print if secret_word was guessed, indicating user wins
if guessed == True:
    print("CONGRATS! YOU WIN! PLEASE PLAY AGAIN")