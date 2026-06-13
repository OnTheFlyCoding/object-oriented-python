import random

#Card Constants
SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')

NCARDS = 8

#Pass in a deck and this function returns random card from the deck
def getCard(deckListIn):
    thisCard = deckListIn.pop() # Remove and return a random card from the deck and return
    return thisCard 

#Pass in a deck and this function returns a shuffled copy of the deck passed
def shuffleDeck(deckListIn):
    deckListOut = deckListIn.copy() # Make a copy of the starting deck
    random.shuffle(deckListOut)
    return deckListOut
#Main Code
print("Welcome to Higher Or Lower!")
print("You have to choose whether the next card to be shown will be higher or lower than the current card.")
print("Getting it right adds 20 points; get it wrong and you lose 15 points.")
print("You have 50 points to start.")
print()

startingDeckList = [] #Empty list that will get filed in the upcoming for loop

for suit in SUIT_TUPLE:#Create the deck of cards
    for thisValue, rank in enumerate(RANK_TUPLE):#For every rank in the rank tuple, assign a value
        cardDict = {'rank':rank, 'suit':suit, 'value':thisValue +1}
        startingDeckList.append(cardDict)

score = 50
#Play the game multiple times
while True:
    print()
    gameDeckList = shuffleDeck(startingDeckList)
    currentCardDictionary = getCard(gameDeckList) #Get the first card from the shuffled deck
    #Unpack the current card
    currentCardRank = currentCardDictionary['rank']
    currentCardSuit = currentCardDictionary['suit']
    currentCardValue = currentCardDictionary['value']
    #Display the current card
    print(f'Starting Card Is: The ', currentCardRank, ' of ' + currentCardSuit)
    print()

    for cardNumber in range(0, NCARDS): #play the game for the number of cards specified 
        answer = input('Will trhe next card be higher or lower than the ' + currentCardRank + ' of ' + currentCardSuit + '? (enter h or l): ')
        answer = answer.lower() #Convert the answer to lowercase for easier comparison
        nextCardDictionary = getCard(gameDeckList) #Get the next card from the shuffled deck
        #Unpack the next card
        nextCardRank = nextCardDictionary['rank']
        nextCardSuit = nextCardDictionary['suit']
        nextCardValue = nextCardDictionary['value']
        #Display the next card
        print(f'Next Card Is: The ', nextCardRank, ' of ' + nextCardSuit)
        print()

        if answer == 'h':
            if nextCardValue > currentCardValue:
                print('Correct! it was higher + 20pts')
                score = score + 20
            else:
                print('Incorrect! It was Lower - 15 pts')
                score = score - 15
        elif answer == 'l':
            if nextCardValue < currentCardValue:
                print('Correct! It was indeed lower! +20 pts')
                score = score +20
            else:
                print('Incorrect! It was Higher - 15pts')
                score = score - 15

        print('Your updated score is: ', score)
        print()
        currentCardRank = nextCardRank
        currentCardValue = nextCardValue #Update the current card value for the next iteration to be compared
        currentCardSuit = nextCardSuit

    goAgain = input('To play again, press Enter, or "q" to quit: ')
    if goAgain == 'q':
        break
    print('Ok Good bye!')
