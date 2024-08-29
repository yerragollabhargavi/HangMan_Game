import random

def get_random_word():
    words = ["python", "javascript", "bootstrap", "html", "css", "coding"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def display_hangman(attempts):
    stages = [
        """
           ------
           |    |
           |    O
           |   \\|/
           |    |
           |   / \\
           |
        """,
        """
           ------
           |    |
           |    O
           |   \\|/
           |    |
           |   / 
           |
        """,
        """
           ------
           |    |
           |    O
           |   \\|/
           |    |
           |    
           |
        """,
        """
           ------
           |    |
           |    O
           |   \\|/
           |    
           |    
           |
        """,
        """
           ------
           |    |
           |    O
           |   \\|
           |    
           |    
           |
        """,
        """
           ------
           |    |
           |    O
           |    |
           |    
           |    
           |
        """,
        """
           ------
           |    |
           |    
           |    
           |    
           |    
           |
        """
    ]
    return stages[attempts]

def play_hangman():
    word = get_random_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print(display_hangman(attempts))
    print(display_word(word, guessed_letters))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
        else:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")

        print(display_hangman(attempts))
        current_display = display_word(word, guessed_letters)
        print(current_display)

        if "_" not in current_display:
            print("Congratulations! You've won!")
            break
    else:
        print(f"Game over! The word was '{word}'.")

if __name__ == "__main__":
    play_hangman()
