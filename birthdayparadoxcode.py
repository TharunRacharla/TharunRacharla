"""Birthday Paradox Simulation, by Al Sweigart al@inventwithpython.com
Explore the surprising probabilities of the "Birthday Paradox".
More info at https://en.wikipedia.org/wiki/Birthday_problem
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, math, simulation"""
"""Again Implemented by Tharun Racharla"""

from ast import While
import datetime, random
from urllib import response

def getBirthdays(numberOfBirthdays):
    """Returns a list of random date objects for birthdays"""
    birthdays = []
    for i in range(numberOfBirthdays):
        """The year is unimportant for our situation, 
        as long as all birthdays have the same year"""
        startOfYear = datetime.date(2001, 1, 1)

        #get a random day into the year:
        randomNumberOfDays = datetime.timedelta(random.randint(0,364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
    """returns a date object of a birthday that occurs more than once in a birthday list."""
    if len(birthdays) == len(set(birthdays)):
        return None #all birthdays are unique so return none.

    #compare each birthday to every other birthdays
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays):
            if birthdayA == birthdayB:
                return birthdayA

#Display the intro
print('Birthday paradox by al sweigart and implemented by Tharun')

#set up a tuple of month names in order
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

while True:
    print('How many birthdays shall i generate ? (Max 50)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 50):
        numBDays = int(response)
        break #user has entered a valid amount
print()

#generate and display the birthdays :
print('Here are', numBDays, 'birthdays:')
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        #Display a comma for each birthday after the first birthday
        print('',end=',')
        monthName = MONTHS[birthday.month - 1]
        dateText = '{} {}'.format(monthName, birthday.day)
        print(dateText, end='')

print()
print()

#determine if there are two birthdays that match
match = getMatch(birthdays)

#display the results:
print('In this simulation, ', end='')
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = '{} {}'.format(monthName, match.day)
    print('multiple people have a birthday on ', dateText)
else:
    print('there are no matching birthdays')
print()

# Run through 100,000 simulatios:]
print('Generating', numBDays, 'random birthdays 100,000 times...')
input('Press enter to begin...')

print('Let\'s run another 100,000 simulations. ')
simMatch = 0 # How many simulations had matching birthdays in them.
for i in range(100_000):
    #Report on the progress every 10,000 simulations:
    if i % 10_000 == 0:
        print(i, 'Simulations run...')
        birthdays = getBirthdays(numBDays)
        if getMatch(birthdays) != None:
            simMatch = simMatch + 1

print('100,000 simulations run')
print(simMatch)

#Display the simulations results:
probability = round(simMatch / 100_000 * 100, 5)
print('Out of 100,000 simulations of', numBDays, 'people, there was a') 
print('matching birthday in that group', simMatch, 'times. This means')
print('that', numBDays, 'people have a', probability, '% chance of')
print('having a matching birthday in their group.')
print('That\'s probably more than you would think')