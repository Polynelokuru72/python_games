import random

words = ["python", "developer", "programming", "hangman"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6

print(" ".join(guessed))

while attempts > 0 and "_" in guessed:
    guess = input("Guess a letter: ").lower()

    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                guessed[i] = letter
    else:
        attempts -= 1
        print(f"Wrong! {attempts} attempts left.")

    print(" ".join(guessed))

if "_" not in guessed:
    print("You win!")
else:
    print(f"You lose! The word was {word}.")
