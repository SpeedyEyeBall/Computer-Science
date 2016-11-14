#Lee-Roy Dobson Week 9 Work
from time import sleep
#Function for retutning multiple totals
def total(beans, returnval):
    red = 0
    green = 0
    for colour in beans:
        if colour.lower() == 'r':
            red += 1
        elif colour.lower() == 'g':
            green += 1
    if returnval == 'red':
        return(red)
    elif returnval == 'green':
        return(green)
    elif returnval == 'total':
        return(len(beans))
    else:
        return(red, green)
    
def main():
    jellyBeans = raw_input('Input your jellybeans[r][g]: ')
    menu()
    userChoice = raw_input('What would you like to do: ')

def checkChoice(choice, beans):
    if choice.lower == 'total':
        print("You have %s beans.") % (total(beans, total))
    elif choice.lower == 'red':
        

def menu():
    print("----------------------------------------------------------")
    print("You can count the [Total], the [Red], [Green] or [Both].")
    sleep(2)
    print("----------------------------------------------------------")
    print("You can also check if it is [Multiple] of 3.")
    sleep(2)
    print("----------------------------------------------------------")
    print("You may check if the jellybeans are [Alternating].")
    sleep(2)
    print("----------------------------------------------------------")
    print("Finally you may check if the total red is [Equal] to the total geen.")
    print("----------------------------------------------------------")
    sleep(2)
