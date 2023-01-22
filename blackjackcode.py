import random, sys

#set up the constants
HEARTS = chr(9829) #character 9829 is '♥'
DIAMONDS = chr(9830) #character 9830 is '♦'
SPADES = chr(9824) #character 9824 is '♠'
CLUBS = chr(9827) #character 9824 is '♣'

BACKSIDE = 'backside'

def main():
    print("""Rules:
            Try to get as close to 21 without going over.
            Kings, Queens, and Jacks are worth 10 points.
            Aces are worth 1 or 11 points.
            Cards 2 through 10 are worth their face value.
            (H)it to take another card.
            (S)tand to stop taking cards.
            On your first play, you can (D)ouble down to increase your bet
            but must hit exactly one more time before standing.
            In case of a tie, the bet is returned to the player.
            The dealer stops hitting at 17""")
    
    money = 5000
    while True: #Main game loop
        # Check if the player has run out pf money
        if money <= 0:
            print("You're Broke!!!")
            print("Good Thing you weren't playing with real money.")
            print("thanks for playing.")
            sys.exit()
        
        #let the player enter their bet for this round
        print('money = ', money)
        bet = getBet(money)

        #Give the dealer and player two cards from the deck each
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        #handle player actions
        print('Bet : ',bet)
        while True: # keep looping until the player stands or busts.
            displayHands(playerHand, dealerHand, False)
            print()

            #check if player has bust:
            if getHandValue(playerHand) > 21:
                break

            #get the player's move, either H, S or D
            move = getMove(playerHand, money - bet)

            #handle the player actions
            if move == 'D':
                #player is doubling down, they can increase their bet:
                additionalBet = getBet(min(bet, (money - bet)))
                bet += additionalBet
                print('Bet increased to {}'.format(bet))
                print('Bet : ', bet)

            if move in ('H', 'D'):
                #Hit/Doubling down takes another card
                newCard = deck.pop()
                rank, suit = newCard
                print('You drew a {} of {}'.format(rank, suit))
                playerHand.append(newCard)

                if getHandValue(playerHand) > 21:
                    # tha player has busted
                    continue

            if move in ('S', 'D'):
                #Stand/Doubling down stops the player's turn:
                break

        #Handle the dealer's action:
        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                #the delaer hits:
                print('Dealer hits...')
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)

                if getHandValue(dealerHand) > 21:
                    break # the dealer is busted
                input('Press enter to continue...')
                print('\n\n')    
                
        #show the final hands
        displayHands(playerHand, dealerHand, True)

        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)

        #Handle whether the player won, lost or tied
        if dealerValue > 21:
            print('Dealer busts ! you win {}'.format(bet))
            money += bet
        elif (playerValue > 21) or (playerValue < dealerValue):
            print('You lost')
            money -= bet
        elif playerValue > dealerValue:
            print('You won {}'.format(bet))
            money += bet
        elif playerValue == dealerValue:
            print("It's a tie, the bet is returned to you.")

        input('Press to continue...')
        print('\n\n')

def getBet(maxBet):
    """Ask the player how much they want to bet for this round"""
    while True: #keep the task until they enter a valid amount
        print('How much do you bet ? (1-{}, or QUIT)'.format(maxBet))
        bet = input('> ').upper().strip()
        if bet == 'QUIT':
            print('Thanks for playing !')
            sys.exit()

        if not bet.isdecimal():
            continue # if player didn't enter a number, ask again

        bet = int(bet)
        if 1<= bet <= maxBet:
            return bet  # player entered a valid bet

def getDeck():
    """Return a list of (rank, suit) tuples for all 52 cards."""
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit)) # Add the numbered cards.
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit)) # Add the face and ace cards
    random.shuffle(deck)
    return deck

def displayHands(playerHand, dealerHand, showDealerHand):
    """Show the player's and dealer's cards. Hide the dealer's first
    card if showDealerHand is False."""
    print()
    if showDealerHand:
        print('DEALER:', getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print('DEALER : ???')
        #hide the dealer's first card:
        displayCards([BACKSIDE] + dealerHand[1:])

    # show the player's cards
    print('PLAYER :', getHandValue(playerHand))
    displayCards(playerHand)

def getHandValue(cards):
    """Returns the value of the cards. Face cards are worth 10.
       aces are worth 11 or 1 (this function picks most suitable ace value)"""
    value = 0
    numberOfAces = 0

    # Add the value for the non-aces:
    for card in cards:
        rank = card[0] # card is a tuple like (rank, suit)
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('K', 'Q', 'J'): # face cards are worth their 10 points.
            value += 10
        else:
            value += int(rank)  # numbered cards are worth their number

    return value

def displayCards(cards):
    """Display all cards in the cards in the cards list"""
    rows = ['', '', '', ''] # the text to diplay on each row

    for i, card in enumerate(cards):
        rows[0] += ' ___ ' #print the top line of the card.
        if card == BACKSIDE:
            #print a cards back:
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            #print the card's front:
            rank, suit = card  #the card is tuple data structure
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, '_'))

    #print each row on the screen:
    for row in rows:
        print(row)

def getMove(playerHand, money):
    """Asks the playerfor their move , and returns 'H' for Hit,'S' for stand and 'D' for double down """
    while True: # Keep looping until the player enters a correct move.
        # Determine what moves the player can make:
        moves = ['(H)it', '(S)tand']

        # The player can double down on their first move, which we can
        #   tell because they'll have exactly two cards:
        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble down')

        # Get the player's move:
        movePrompt = ', '.join(moves) + '> '
        move = input(movePrompt).upper()
        if move in ('H', 'S'):
            return move # Player has entered a valid move.
        if move == 'D' and '(D)ouble down' in moves:
            return move # Player has entered a valid move.

 # If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()