import random
import string


class Hangman:
    letter_in_word = 'in-word'
    letter_not_in_word = 'not-in-word'
    letter_already_uncovered = 'uncovered'
    letter_not_ascii_lowercase = 'not-ascii-lowercase'
    letter_not_single = 'not-single'
    letter_entered_before = 'entered-before'

    def __init__(self, init_words=None, init_lives=8):
        if init_words is None:
            init_words = ['python', 'java', 'kotlin', 'javascript']
        self.words = init_words
        self.lives = init_lives
        self.chosen_word = random.choice(self.words)
        self.blind_word = list('-' * len(self.chosen_word))
        self.current_letter = None
        self.word_uncovered = False
        self.letters_entered_before = []

    def start(self):
        print('H A N G M A N')
        option = None

        while option != 'play' and option != 'exit':
            option = input('Type "play" to play the game, "exit" to quit: ').strip()

        if option == 'play':
            while self.lives > 0:
                self.insert_letter()
                letter_status = self.check_letter()
                if not self.word_uncovered:
                    print(self.show_result(letter_status))
                else:
                    break
            self.game_over(self.has_winner())
        elif option == 'exit':
            return

    def insert_letter(self):
        self.current_letter = self.get_letter()

    def show_result(self, letter_status):
        if letter_status == Hangman.letter_not_single:
            return 'You should print a single letter'
        elif letter_status == Hangman.letter_not_ascii_lowercase:
            return 'It is not an ASCII lowercase letter'
        elif letter_status == Hangman.letter_in_word:
            self.letters_entered_before.append(self.current_letter)
            return ''
        elif letter_status == Hangman.letter_already_uncovered or letter_status == Hangman.letter_entered_before:
            return 'You already typed this letter'
        elif letter_status == Hangman.letter_not_in_word:
            self.letters_entered_before.append(self.current_letter)
            return 'No such letter in the word'

    def check_letter(self):
        if len(self.current_letter) != 1:
            return Hangman.letter_not_single
        elif self.current_letter not in string.ascii_lowercase:
            return Hangman.letter_not_ascii_lowercase
        elif self.current_letter in self.letters_entered_before:
            return Hangman.letter_entered_before
        elif self.current_letter in self.chosen_word:
            current_blind_word = ''.join(self.blind_word)
            self.update_blind_word()
            if self.is_blind_word_updated(current_blind_word):
                return Hangman.letter_in_word
            else:
                return Hangman.letter_already_uncovered
        else:
            self.lives -= 1
            return Hangman.letter_not_in_word

    def get_letter(self):
        print('\n' + ''.join(self.blind_word))
        return input('Input a letter: ').strip()

    def update_blind_word(self):
        indices = [i for i in range(len(self.chosen_word)) if self.chosen_word[i] == self.current_letter]
        for i in indices:
            self.blind_word[i] = self.current_letter
        if self.is_word_uncovered():
            self.word_uncovered = True

    def is_blind_word_updated(self, current_blind_word):
        if ''.join(self.blind_word) == current_blind_word:
            return False
        return True

    def has_winner(self):
        return self.is_word_uncovered()

    def is_word_uncovered(self):
        if self.chosen_word == ''.join(self.blind_word):
            return True
        return False

    def game_over(self, winner=False):
        if winner:
            print(f"You guessed the word {self.chosen_word}!\nYou survived!")
        else:
            print("You are hanged!")


game = Hangman()
game.start()
