"""
Author: Lani Hurley
Date: 5/13/2022
Filename: hangman.py
Program is a simple hangman game with ASCII art.
*Must include files: hangman_art.py and hangman_words.py in same folder/directory as hangman.py to run file
*Must import random python package to run file
"""
import random
from hangman_art import stages, logo
from hangman_words import word_list

print(logo)
game_is_finished = False
lives = len(stages) - 1

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display += "_"

while not game_is_finished:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print("Game Over...You Lose!")

    if "_" not in display:
        game_is_finished = True
        print("You win!")

    print(stages[lives])
