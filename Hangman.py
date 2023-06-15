import random

class Hangman:
    def __init__(self, word_list):
        self.word_list = word_list
        self.secret_word = ""
        self.guessed_letters = []
        self.num_guesses = 6

    def select_word(self):
        self.secret_word = random.choice(self.word_list)

    def display_word(self):
        displayed_word = ""
        for letter in self.secret_word:
            if letter in self.guessed_letters:
                displayed_word += letter + " "
            else:
                displayed_word += "_ "
        print(displayed_word)

    def guess_letter(self, letter):
        self.guessed_letters.append(letter)
        if letter not in self.secret_word:
            self.num_guesses -= 1

    def check_win(self):
        for letter in self.secret_word:
            if letter not in self.guessed_letters:
                return False
        return True

    def play(self):
        print("Welcome to Hangman!")
        self.select_word()

        while self.num_guesses > 0:
            print("\nGuesses left:", self.num_guesses)
            self.display_word()

            guess = input("Guess a letter: ").lower()

            if len(guess) != 1:
                print("Please enter a single letter!")
                continue

            if guess in self.guessed_letters:
                print("You've already guessed that letter!")
                continue

            self.guess_letter(guess)

            if self.check_win():
                print("Congratulations! You've guessed the word:", self.secret_word)
                return

        print("Game over! You've run out of guesses. The word was:", self.secret_word)


# List of words for the game
words = ["hangman", "python", "computer", "programming", "game"]

# Create an instance of the Hangman class
hangman_game = Hangman(words)

# Play the game
hangman_game.play()
