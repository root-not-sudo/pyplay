import string


def variableName(name):

    dict = string.ascii_letters + string.digits + '_'
    if name[0] in string.digits:
        return False
    else:
        for i in name:
            if not i in dict:
                return False
        return True
