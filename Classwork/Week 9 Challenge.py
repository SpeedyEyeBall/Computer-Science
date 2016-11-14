#Lee-Roy Dobson Week 9 Work
from time import sleep
#Function for retutning multiple totals. Inputs [red][green][total][both]
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
#Functiopn for checking if it is a multiple of 3.
def check3(beans):
    state = 0
    for bean in beans:
        if state == 2:
            state = 0
        else:
            state += 1
    if state == 0:
        return(True)
    else:
        return(False)
#Function for checking if the beans alternate. 
def checkaltern(beans):
    prevbean = ''
    for bean in beans:
        if prevbean == '':
            prevbean = bean
        else:
            if bean != prevbean:
                prevbean = bean
            else:
                return(False)
    return(True)

def makeChoice(choice, beans):
    if choice.lower == 'total':
        return("You have %s beans.") % (total(beans, 'total'))
    elif choice.lower == 'red':
        return("You have %s red beans.") % (total(beans, 'red'))
    elif choice.lower == 'green':
        return("You have %s green beans.") % (total(beans, 'green'))
    elif choice.lower == 'both':
        return("You have %s red beans.") % (total(beans, 'both'))
    elif choice.lower == 'multiple':
        if check3(beans):
            return("The total beans is a multiple of 3.")
        else:
            return("The total beans is not a multiple of 3.")
    elif choice.lower == 'alternating':
        if checkaltern(beans):
            return("The beans alternate.")
        else:
            return("The beans do not alternate.")
    
        
        
#Function for showing the menu
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
#Main function    
def main():
    jellyBeans = raw_input('Input your jellybeans[r][g]: ')
    menu()
    userChoice = raw_input('What would you like to do: ')
    print(makeChoice(userChoice))
