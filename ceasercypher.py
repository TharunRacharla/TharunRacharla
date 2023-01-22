from urllib import response
import pyperclip as pc
#Every possible symbol that can be encrypted/decrypted:
# (!) You can add numbers and punctuation marks to encrypt those symbols as well
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('Ceaser cipher')
print('The Ceaser cipher encrypts letters by shifting over by a key number')
print('For example, a key of 2 means a letter A is encrypted to C, the letter B encrypted to D, and so on')
print()

#Let the user enter if they are encrypting or decrypting :
while True: #keep asking until until user enters values e r d
    print('Do you want to (e)ncrypt or (d)ecrypt ?')
    response = input('> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print('please enter the letter e or d')

# Let the user enter the key to use:
while True: # kepp asking until user enters a valid key:
    maxKey = len(SYMBOLS) - 1
    print('Please enter the key (0 to {}) to use'.format(maxKey))
    response = input('> ').upper()
    if not response.isdecimal():
        continue

    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break

# Let the user to enter the message to encrypt/decrypt
print('Enter the message to {}'.format(mode))
message = input('> ')

#ceaser cypher only works on upper letters:
message = message.upper()

# stores the encrypted / decrypted form of message 
translated = ''

#encrypt/decrypt each symbol in messsage:
for symbol in message:
    if symbol in SYMBOLS:
        #Get the encrypted (/decrypted) number of this symbol
        num = SYMBOLS.find(symbol) # get the number of symbol
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key
        
        #Handle the wrap around if num is larger than the length of SYMBOLS or less than 0
        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)

        #add encrypted/decrypted number's symbol to translated:
        translated = translated + SYMBOLS[num]
    else:
        #Just add the symbol without encryption / decryption;
        translated = translated + symbol

#Display the encrypted/decrypted string to the screen
print(translated)

try:
    pc.copy(translated)
    print('Full {}ed text copied to clipboard.'.format(mode))
except:
    pass # do nothing if pyperclip wasn't installed