#Lee-Roy Dobson Week 9 Work
jellyBeans = raw_input('Input your jellybeans[r][g]: ')

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
print(check3(jellyBeans))
