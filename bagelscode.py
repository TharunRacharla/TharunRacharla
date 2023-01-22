import random
num_digits = 3
max_guesses = 10


def main():
    print("I am thinking of a {}- digit number with no repeated digits.")
    print("Bagels, a deductive logic game by Al Sweigart al@inventwithpython.com")
    print("""Try to guess what it is. Here are some clues: 
            When i say :    That means:
                pico        One digit is correct but in the wrong position
                Fermi       One digit is correct and in the right position
                Bagels      No digit is corect
            For example, if the secret number was 248 and your guess was 843, the clues would be Fermi pico""".format(num_digits))
    while True: #main game loop
        #this stores the secret number the player needs to guess
        secretNum = getSecretNum()
        print("I've thought up a number")
        print("You have {} guesses to get it.".format(max_guesses))

        numGuesses = 1
        while numGuesses <= max_guesses:
            guess = ''
            #keep looping until they enter a valid guess:
            while len(guess) != num_digits or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1
                
            if guess == secretNum:
                break # They're correct, so break out of this loop
            if numGuesses > max_guesses:
                print('You ran out of guesses')
                print('The answer was {}.'.format(secretNum))

        #Ask player if they want to play again.
        print('Do you want to play again ? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing.')

def getSecretNum():
    """"Returns a string made up of num_digits."""
    numbers = list('0123456789') # Create a list of digits 0 to 9
    random.shuffle(numbers) # Shuffle them into random order.

    #get the num_digits in the list for the secret number:
    secretNum = ''
    for i in range(num_digits):
        secretNum += str([i])
    return secretNum

def getClues(guess, secretNum):
    """Returns a string with the pico , fermi and Bagels clues for a guess and secret number pair."""
    if guess == secretNum:
        return 'you got it!'
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # A correct digit is in the correct place
           clues.append('Fermi') 
        elif guess[i] in secretNum:
            #a correct digit is in incorrect place
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels' # There are no correct digits at all
    else:
        # sort the clues in an alphabetical order so that 
        # their original order gave information away
        clues.sort()
        #make a single string from a list of string clues.
        return ' '.join(clues)

if __name__ == '__main__':
    main()