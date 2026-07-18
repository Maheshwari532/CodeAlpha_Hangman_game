import random

words_list = ["Sunshine","Keyboard","Hello","Computer","Planet"]

actual_word = random.choice(words_list).lower()
attempts = 6
guess_list = []

while attempts > 0:
   
    
    for char in actual_word:
        if char in guess_list:
            print(char, end=" ")
        else:
            print("_", end=" ")
            

    char_guess = input("\nGuess a character:")

    if char_guess in actual_word:
        guess_list.append(char_guess)
        print("Correct!")
        
    else:
        attempts -= 1
        print("\nWrong! Attempts left:", attempts)
        
    
    if all(ch in guess_list for ch in actual_word):
        print("\nYou Won! Word was:", actual_word)
        break

if attempts == 0:
    print("\nGame Over! Word was:", actual_word)

