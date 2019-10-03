def isPangram(potentialPangram):
    potentialPangram.lower()
    alphaCounter = []
    for i in 'abcdefghijklmnopqrstuvwxyz':
        if i in potentialPangram:
            alphaCounter.append(i)
    return len(alphaCounter) == 26
    
print(isPangram('The quick brown fox jumped over the lazy dogs'))
print(isPangram('Brent Markus.'))

