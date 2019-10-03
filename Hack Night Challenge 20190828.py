def nameShuffle(fullName):
    if ' ' not in fullName:
        return fullName
    newName = fullName.split(' ')
    return newName[len(newName)-1] + ", " +  " ".join(newName[0:len(newName)-1])
   
print(nameShuffle('Brent Markus'))
print(nameShuffle('John Wilkes Booth Retired'))
print(nameShuffle('Cher'))
