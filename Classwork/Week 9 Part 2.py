#Lee-Roy Dobson Week 9 Work
jellyBeans = raw_input('Input your jellybeans[r][g]: ')

def countColour(beans, returnval):
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
    else:
        return(red, green)

print(countColour(jellyBeans, 'both'))
