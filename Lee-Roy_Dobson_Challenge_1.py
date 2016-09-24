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
def draw_hand(counter):
    print("You drew:")
    #Loops for the number of cards we want to generate
    while counter > 0:
        print("%s of %s, ") % (suit(), rank())
        counter -= 1
    
#Function for getting and checking the users input is an int
def hand_input():
    #Gets the users desired hand size
    hand_size = int(raw_input("How many cards do you wish to draw?"))
    #Checks to make sure that it is an integer
    if type(hand_size == type(1)):
        draw_hand(hand_size)
    else:
        print("This is not an integer (A whole number)")
        

#While loop allows them to draw another hand if they wish
while 1 == 1:
    #Promt the user and get their input
    user_input = raw_input("Draw a new hand? Yes or No?: ")
    #Check the users input
    if user_input.lower() == "yes":
        hand_input()
    elif user_input.lower() == "no":
        break
    else:
        print("Unknown command")
    
