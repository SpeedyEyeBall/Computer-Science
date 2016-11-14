#Lee-Roy Dobson Week 9 Work
jellyBeans = raw_input('Input your jellybeans[r][g]: ')

def checksame(beans):
    stack = 0
    for colour in beans:
        if colour.lower() == 'r':
            stack += 1
        else:
            stack -= 1
    if stack == 0:
        return(True)
    else:
        return(False)

print(checksame(jellyBeans))
