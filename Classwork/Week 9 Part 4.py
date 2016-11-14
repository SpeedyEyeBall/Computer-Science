#Lee-Roy Dobson Week 9 Work
jellyBeans = raw_input('Input your jellybeans[r][g]: ')

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

print(checkaltern(jellyBeans))
