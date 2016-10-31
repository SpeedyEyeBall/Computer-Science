#Lee-Roy Dobson
from random import randint

#Function to create a card
def generateCard():
    card = {
        'suit': suit(),
        'rank': rank()
    }
    return(card)

#Function for generating the suit
def suit():
    randomnumber = randint(1, 4)
    if randomnumber == 1:
        return("Spades")
    elif randomnumber == 2:
        return("Clubs")
    elif randomnumber == 3:
        return("Hearts")
    else:
        return("Diamonds")

#Function for generating the card rank
def rank():
    #Generate a random number between 1 and 13 inclusive
    randomnumber = randint(1,13)
    #Check if the number corresponds with a rank
    if randomnumber == 1:
        return("Ace")
    elif randomnumber == 11:
        return("Jack")
    elif randomnumber == 12:
        return("Queen")
    elif randomnumber == 13:
        return("King")
    else:
        return(randomnumber)

def main():
    #Generate the random card
    card1 = generateCard()
    print("You draw the card, %s of %s") % (card1['rank'], card1['suit'])
    userGuess = raw_input("Will the next card be [Higher] or [Lower]: ")
    card2 = generateCard()
    if userGuess.lower() == 'higher':
        if cardScore(card1) <= cardScore(card2):
            print("Correct! The next card was the %s of %s.") % (card2['rank'], card2['suit'])
        else:
            print("Wrong! The next card was %s of %s.")% (card2['rank'], card2['suit'])
    elif userGuess.lower() == 'lower':
        if cardScore(card1) >= cardScore(card2):
            print("Correct! The next card was the %s of %s") % (card2['rank'], card2['suit'])
        else:
            print("Wrong! The next card was %s of %s.")% (card2['rank'], card2['suit'])
   
def cardScore(card):
    cardScoreVal = 0
    if card['rank'] == 'Ace':
        cardScoreVal = 1
    elif card['rank'] == 'Jack':
        cardScoreVal = 11
    elif card['rank'] == 'Queen':
        cardScoreVal = 12
    elif card['rank'] == 'King':
        cardScoreVal = 13
    else:
        cardScoreVal = card['rank']
    return(cardScoreVal)

main()
