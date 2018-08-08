import time, random
from hangmanBody import draw_hangman
from wordList import word_list

def greet_user():
    """Greets the user before starting the game. Returns name of player. 
    """

    player = input("Hello!\nWhat is your name?").title()
    
    print("Well {}, I hope you're ready for the game of your life... we're about to play...".format(player))
    
    sleep_counter = 0
    while sleep_counter <= 3:
        time.sleep(1)
        print("...")
        sleep_counter += 1

    print("HANGMAN! \n")
    time.sleep(1)
    print("DUN DUN DUN!")
    print()
    time.sleep(1)

    return player

def difficulty_level():
    """Asks the user to choose their difficulty level.
    
    An "easy" game will return one word, a "medium" game will return two words, and a "hard" game will return three words. 
    """
    
    # Lists with choices for the following if statements 
    easy_options = ["1", "E"]
    medium_options = ["2", "M"]
    hard_options = ["3", "H"]
    options = [easy_options, medium_options, hard_options]

    # List of viable print statement options depending on the level of difficulty.
    print_statement_options = ["You have chosen: Easy.\nWise choice my friend, wise choice.", "You have chosen: Medium\nYou're pretty brave to choose something so challenging.", "You have chosen: Hard\nA man's life is on the line and you're choosing the hardest option!? Really?!"]

    try_again = True

    while try_again:

        level_of_difficulty = (input("Choose your difficulty level: \n(1) Easy\n(2) Medium\n(3) Hard\n").title()[0])
                
        for level in options:
          
            if level_of_difficulty not in options[0] and level_of_difficulty not in options[1] and level_of_difficulty not in options[2]:
                print("That was not an option. Please try again.")
                index = 5
                # Break statement stops "That was not an option being printed 3 times within the for-loop."
                break

            elif level_of_difficulty in level:
                
                level_of_difficulty = level[0]

                index = (int(level_of_difficulty) - 1)
                print(print_statement_options[index])
                # Setting try_again to False exists the while loop
                try_again = False
                break
        
        if index in options:
            break

    return int(level_of_difficulty)

def choose_words():

    print("Are you ready for the most exciting game of Hangman of your life!?")
    time.sleep(1)
    print("\nI hope so, because ready or not, it is about to begin!")
  
    hangman_word = random.choice(word_list)

    return hangman_word

def update_dashes(secret_word, current_dashes, part_of_answer):
    """This function updates the number of dashes with letters when the dashes are correct. 
    """
    result = ""

    for i in range(len(secret_word)):
        if secret_word[i] == part_of_answer:
            
            # Adds guess to string if the guess is correct
            result = result + part_of_answer
        
        else:
            result = result + current_dashes[i]

    return result 

def get_guess(word, level_of_difficulty):
    """This function takes the input of choose_words() and prints out the number of remaining guesses a user has, as well as the Hangman Picture itself. 
    
    The difficulty_level also affects the number of guesses.
    """

    alphabet_string = "abcdefghijklmnopqrstuvwxyz"
  
    previous_guesses = []
    
    # Guesses remaining is contingent upon level_of_difficulty 
    guesses_remaining_options = [6, 5, 4]
    
    index = level_of_difficulty - 1
    guesses_remaining = guesses_remaining_options[index]

    dashes = "-" * len(word)

    print("You have", guesses_remaining, "total guesses this round and there are", len(word), "total letters in the word(s).")
    print(dashes)

    # Both guesses_remaining needs to be greater than 0 and the dashes cannot be the secret word in order to enter this while loop.
    while guesses_remaining > 0 and not dashes == word:

        guess = input("What is your guess?").lower()

        # Invalid input: Too many letters in guess when the guess is not correct
        if guess == word:
            print("CONGRATS! YOU SAVED HIM!!!!!")
            break 
        
        elif len(guess) != 1:
            print("Your guess must be exactly one character in length. (Note: You do not lose a guess for this.)")
        
        # Invalid input: The guess was already guessed
        elif guess in previous_guesses:
            print("Sorry, you've already guessed {}. You can't guess it again this round. (Note: You do not lose a guess for this.)".format(guess))
        
        elif guess not in alphabet_string:
            print("Sorry, your guess must be a standard English letter. {} is not valid. Guess again. (Note: You do not lose a guess for this.)".format(guess.title()))

        # If guess is not in the word(s)
        elif guess not in word:
            
            # Decriments remaining guesses before printing remaining_guesses to the screen
            guesses_remaining -= 1
            print("Sorry, {} isn't in the word. Guess again. You have {} guesses remaining.".format(guess, guesses_remaining))

            previous_guesses.append(guess)

            draw_hangman(level_of_difficulty, guesses_remaining)
            

        # If guess is in the word
        elif guess in word:
            
            print("That letter is in your word. Good job.")
            dashes = update_dashes(word, dashes, guess)
            print(dashes)

            previous_guesses.append(guess)
        else:
            print("Good job. I didn't think of this edge case but you found it! At least I thought of this else statement to send you back to the top of the loop!")


    if guesses_remaining == 0:
       
        print("Oh no! You hanged an innocent man! By the way, the word was {}".format(word))
        
    elif dashes == word:
        print("YOU SAVED HIM!!!!! Congrats, you've won!")

    return guesses_remaining

def play_hangman():
    """This funtion runs the body of the code by calling other functions.
    
    The function is a big while loop in case the player wants to play again.
    """
    play_again = "y"

    while play_again = "y":
      
        greet_user()
     
        # Asks user what difficultly level they want
        challenge_level = difficulty_level()

        words_to_guess = choose_words()

        get_guess(words_to_guess, challenge_level)

        play_again = input("Would you like to play again? (Y/N) ").lower()[0]
        
        while True:
            if play_again == "n":
                print("Goodbye!")
                break
            
            elif play_again != "y":
                print("Not a valid response")
play_hangman()


""" Funny things I debugged:
1) Printing multiple dashes  
2) Simplifying my difficulty_level function
"""
