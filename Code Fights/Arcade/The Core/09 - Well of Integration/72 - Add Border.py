def addBorder(picture):

    border_len = len(picture[0]) + 2
    picture.append('*' * border_len)
    picture.insert(0, '*' * border_len)
    for i in range(1, len(picture)-1):
        picture[i] = "*" + picture[i] + "*"
    return picture
