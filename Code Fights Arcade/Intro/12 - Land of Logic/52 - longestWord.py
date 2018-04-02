import string


def longestWord(text):
    a, count, max = [], 0, 0

    for i in range(len(text)):
        if i == len(text) - 1:
            a.append(text[count:i+1])
        if text[i] not in string.ascii_letters:
            if text[i-1] in string.ascii_letters:
                a.append(text[count:i])
            count = i + 1

    if count == 0:
        return text

    for i in a:
        if len(i) > max:
            max = len(i)
            word = i

    return word


print(longestWord("Ready, steady, zoooooo"))
