# there's a lot of uselessness in this, but whatever...
def isSubstitutionCipher(string1, string2):

    string1_std, string2_std = 'A', 'A'
    alpha1, alpha2 = 'A', 'A'
    for i in range(1, len(string1)):
        if string1[i] in string1[0:i]:
            string1_std += string1[i]
        else:
            alpha1 = chr(ord(alpha1) + 1)
        if string2[i] in string2[0:i]:
            print('poop')
        else:
            alpha2 = chr(ord(alpha2) + 1)
        if alpha1 != alpha2:
            return False
    return True
