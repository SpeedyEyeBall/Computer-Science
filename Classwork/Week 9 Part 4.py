#Lee-Roy Dobson Week 9 Work
jellyBeans = raw_input('Input your jellybeans[r][g]: ')
#Function takes 1 parameter, the string of beans.
def checkaltern(beans):
    prevbean = '' #variable for storing the previous bean.
    for bean in beans:  #For loop runs through each character of the string
        if prevbean == '': #checks if it's the first time looping.
            prevbean = bean 
        else: 
            if bean != prevbean: #Is the current bean the same as the last?
                prevbean = bean #Set the prevbean to the current bean
            else:
                return(False)
    return(True) #Returns true if the for loop completes without returning false.

print(checkaltern(jellyBeans))
