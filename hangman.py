import random

words = ['python', 'developer', 'hangman', 'keyboard', 'programming']
word = random.choice(words)
guessed = ["_"] * len(word)
attempts_left = 6
guessed_letters = set()

print("🪓 Welcome to Hangman!")

while attempts_left > 0 and "_" in guessed:
    print("\nWord: " + " ".join(guessed))
    print(f"Guessed letters: {', '.join(guessed_letters)}")
    print(f"Attempts left: {attempts_left}")
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single valid letter.")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.add(guess)

    if guess in word:
        for idx, letter in enumerate(word):
            if letter == guess:
                guessed[idx] = guess
    else:
        print(f"Nope, the letter '{guess}' is not in the word.")
        attempts_left -= 1

# Game result
if "_" not in guessed:
    print(f"\n🎉 You won! The word was '{word}'")
else:
    print(f"\n💀 Game over! The word was '{word}'")
