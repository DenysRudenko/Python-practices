# -----------------------------------------------------------
# Desctiption:
# Hangman game,the first part it`s a game without hints.
# The other part of the game helps the user to play the game,by showing clues.
# See details at the end of the code...
#
# (C) 2021 Rudenko Denys, Kiev, Ukraine
# Released for KPI,Python practices lections
# email: heartbreathing19951014@gmail.com
# -----------------------------------------------------------

"""Fist part without a clues"""
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words(WORDLIST_FILENAME):
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

wordlist = load_words(WORDLIST_FILENAME)

def select_word(wordlist):
    return random.choice(wordlist)

def get_guessed_word(secret_word, letters_guessed):
    letter_list = []
    for letter in secret_word:
        if letter in letters_guessed:
            letter_list.append(letter)
        else:
            letter_list.append("_ ")
            
    return "".join(letter_list)

def is_word_guessed(secret_word, letters_guessed):
    first_set = set(secret_word)
    second_set = set(letters_guessed)
    difference = first_set - second_set
    return len(difference) == 0

def get_available_letters(letters_guessed):
    available_letters = []
    abc = string.ascii_lowercase
    for letter in abc:
        if letter not in letters_guessed:
            available_letters.append(letter)
    return "".join(available_letters)


 #-----------------------------------------------------------
#def match_with_gaps(my_word, other_word):
#    new_word = my_word.replace(" ", "")
#    if len(new_word) != len(other_word):
#        return False
#    for i in range(len(other_word)):
#        if new_word[i] == "_":
#            if other_word[i] in new_word:
#                return False
#        else:
#            if new_word[i] != other_word[i]:
#                return False
#    return True

# def show_possible_matches(my_word):   
#    matched_words = []
#    for word in wordlist:
#        if match_with_gaps(my_word, word):
#            matched_words.append(word)
#    if len(matched_words) == 0:
#        print("No matches found")
#    else:
#        print(" ".join(matched_words))
#-----------------------------------------------------------       

def hangman_with_hints(secret_word):
    letters_guessed = []
    guesses_remaining = 6
    warnings_remaining = 3
    vowels = "aeiou"

    print("Welcome to the game Hangman!")
    print(f'I am thinking of a word that is {len(secret_word)} letters long.')
    print(f'You have {warnings_remaining} warnings left.')
   
    while (guesses_remaining > 0) and not is_word_guessed(secret_word, letters_guessed):
        print("-" * 12)
        print(f'You have {guesses_remaining} guesses left.')
        print(f'Available letters: {get_available_letters(letters_guessed)}')

        wrong_input = False
        letter = input("Please guess a letter:")
#-----------------------------------------------------------        
#        if letter == "*":
#            print('Possible word matches are: ', end="")
#            show_possible_matches(get_guessed_word(secret_word, letters_guessed ))
#            continue
#-----------------------------------------------------------
        if len(letter) == 0:
            print("Oops! This is no input letter. ", end="")
            wrong_input = True
        
        elif len(letter) > 1:
            print(f'Opps! You have entered {len(letter)} letters. ', end="")
            wrong_input = True
        else:
            if letter.lower() not in string.ascii_lowercase:
                print(f'Oops! "{letter}" is not a valid letter. ', end="")
                wrong_input = True
            else:
                letter = letter.lower()
                if letter in letters_guessed:
                    print("Opps! You`ve alredy guessed that letter. ", end="")
                    wrong_input = True
                
        if wrong_input:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print(f'You have {warnings_remaining} warnings left: ', end="")
            else:
                guesses_remaining -= 1
          
        else:
            letters_guessed.append(letter)
            if letter in secret_word:
                print("Good gueess: ", end="")
            else:
                guesses_remaining -= 2 if letter in vowels else 1    
                print("Oops! That letter is not in my word: ", end="")

        print(get_guessed_word(secret_word, letters_guessed ))
    
    print("-" * 12)
    
    if guesses_remaining > 0:
        total_score = guesses_remaining * len(set(secret_word))
        print(f'Congratulations, you won! Your total score for this game is: {total_score}.')
    else:
        print(f'Sorry, you ran out of guesses. The word was {secret_word}.')

secret_word = select_word(wordlist)
hangman_with_hints(secret_word)    

#--------------------------------------------------------------------------------------------------------------
    #To play "Hangman" without clues you dont change anything there.
    #To play "Hangman_with_clues" you should uncomment 2 functions:-"def match_with_gaps(my_word, other_word)",
    # and "def show_possible_matches(my_word)".Also you should uncomment in the last function:-"def hangman_with_hints(secret_word)",
    # a condition "if letter == "*",and till "if len(letter) == 0"


