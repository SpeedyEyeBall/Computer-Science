#Lee-Roy Dobson
from Tkinter import *
from random import randint

directory = 'card_images\\'

def directory():
    card_number = randint(1, 52)
    return("card_images\\" + str(card_number) + ".gif")


       
def main():
    #Initialise window root
    root = Tk()
    card_image = PhotoImage(file = directory())
    card = Label(root, image = card_image)
    card.image = card_image
    card.pack()

    def generateCard():
        card_image = PhotoImage(file = directory())
        card.configure(image = card_image)
        card.image = card_image

    #Initialise a button that executes generateCard()
    button_generate = Button(root, text = "New Card", command = lambda: generateCard())
    button_generate.pack(side = BOTTOM)
    #End of mainloop
    root.mainloop()


main()
