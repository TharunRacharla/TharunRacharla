print('Caesar Cipher Hacker, by Al Sweigart al@inventwithpython.com')

# let the user specify the message to hack;
print('Enter the encrypted ceaser cypher message to hack:')
message = input('> ').upper()

# Every possible symbol that can be encrypted/decrypted
#(!) This must matchthe SYMBOLS used whille encrypting the message
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(SYMBOLS)): #loop through every possible key
    translated = ''

    #decrypt each symbol in the message:
    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol) # Get the number of the symbol
            num = num - key # decrypt the number

            # Handle the wrap around if the number is less than zero:
            if num < 0:
                num = num + len(SYMBOLS)

            # add decrypted number's symbol to translated:
            translated = translated + SYMBOLS[num]
        else:
            #just add the symbol withuot decrypting
            translated = translated + symbol

    # display the key being tested, along with it's decrypted text:
    print(' Key #{}: {}'.format(key, translated))