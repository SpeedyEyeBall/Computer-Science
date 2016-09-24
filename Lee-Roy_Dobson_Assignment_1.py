#Lee-Roy Dobson
from random import randint

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
    #Generate a random number between 1 and 3 inclusive
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

#While loop allows them to draw many cards
while 1 == 1:
    #Promt the user and get their input
    user_input = raw_input("Draw a card? Yes or No?: ")
    #Check the users input
    if user_input.lower() == "yes":
        print("You draw a %s of %s") % (rank(), suit())
    elif user_input.lower() == "no":
        break
    else:
        print("Unknown command")
    
