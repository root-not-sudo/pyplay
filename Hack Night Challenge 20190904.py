#import string as str
""""def isIsogram(possibleIsogram):
    possibleIsogram.lower()
    for i in range(len(possibleIsogram)-1):
        for j in range(i+1, len(possibleIsogram)):
            if possibleIsogram[j].isalpha():
                if possibleIsogram[i] == possibleIsogram[j]:
                    return False

    return True
"""

def isIsogram(possibleIsogram):
    possibleIsogram.lower()
    characters = {}
    for letter in possibleIsogram:
        if letter.isalpha():
            if letter in characters.keys():
                return False
            characters.update({letter : '1'})
    return True    
    
print(isIsogram('lumberjacks'))
print(isIsogram('background'))
print(isIsogram('downstream'))
print(isIsogram('six-year-old'))
print(isIsogram('challenge'))
print(isIsogram('Abinidai'))
print(isIsogram('isograms'))
print(isIsogram('starting'))
print(isIsogram('Brent Markus'))
