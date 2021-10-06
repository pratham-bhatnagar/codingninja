import random
import time
from words import wordlist


def get_word():
    word = random.choice(wordlist)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("LETS PLAY HANGMAN! \n\n")

    time.sleep(1)
    print(display(0))
    print("\n")
    print(word_completion)
    print("\n")
    print("( TIP! WORD IS",len(word)," LETTERS LONG. ")
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        time.sleep(0.5)
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter ! ", guess)
            elif guess not in word:
                print(guess, " is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                index = word.find(guess)
                word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                print ("\n\nCorrect! \nYour guesses: %s" % (guessed_letters))
                print(str(word_as_list))

                if '_' not in word_completion:
                    guessed=True

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        
        elif guess=="QUIT" or guess=="EXIT":
            quit()
        else:
            print("Not a valid guess.")

        
        
        print(display(tries))
        print(word_completion)
        print("\n")
        time.sleep(0.5)
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")


def display(tries):
    hang = ["""
    H A N G M A N 

    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    =========""", """
    H A N G M A N 

    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    =========""", """
    H A N G M A N 

   +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========""", """
    H A N G M A N 

    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========""", """
    H A N G M A N 

    +---+
    |   |
    O   |
    |   |
        |
        |
    =========""", """
    H A N G M A N 

    +---+
    |   |
    O   |
        |
        |
        |
    =========""", """
    H A N G M A N 
    +---+
    |   |
        |
        |
        |
        |
    ========="""]
    return hang[tries]



word = get_word()
play(word)
time.sleep(1)
while input("Play Again? (Y/N) ").upper() == "Y":
    word = get_word()
    play(word)
