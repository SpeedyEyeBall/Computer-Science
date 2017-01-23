#Lee-Roy Doboson
#This is a program to show some facts on the Chinese new year and to present a fortune
from random import randint

def main():
    print('On Saturday, January 28 the Chinese new year will begin. \nIt is the year of the Rooster.\nA fortune cookie is opened to see what the year will be like.')
    if askUser() ==  True:
        print(giveFortune())
    else:
        print("Enjoy the new year.")
        
def askUser():
    userOpenCookie = raw_input("\nDo you want to open a fortune cookie?[Yes][No]: ")
    while True:
        if userOpenCookie.lower() == "yes":
            return(True)
        elif userOpenCookie.lower() == "no":
            return(False)
        else:
            userOpenCookie = raw_input("Not a correct input. Enter [Yes] or [No]: ")

def giveFortune():
    fortunes = open('fortunes.txt', 'r+')
    lines = sum(1 for line in open('fortunes.txt'))
    for i in range(1,randint(1,lines)-1):
        fortunes.readline()
    return(fortunes.readline())

if __name__ == '__main__':
    main()
