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

#Function for printing the hand to the user
def draw_deck():
    print("Your deck order is:")
    counter = 52
    #Loops for the number of cards we want to generate
    while counter > 0:
        print("%s of %s, ") % (rank(), suit())
        counter -= 1
    
#While loop allows them to draw another hand if they wish
while 1 == 1:
    #Promt the user and get their input
    user_input = raw_input("Draw a new deck? Yes or No?: ")
    #Check the users input
    if user_input.lower() == "yes":
        draw_deck()
    elif user_input.lower() == "no":
        break
    else:
        print("Unknown command")
    
