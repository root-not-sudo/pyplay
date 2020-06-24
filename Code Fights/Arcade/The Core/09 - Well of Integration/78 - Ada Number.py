def adaNumber(line):

    line = line.lower()
    line = line.replace('_', '')
    if line is '':
        return False

    if '#' not in line:
        return parseDecimal(line)

    if line.count('#') != 2 or line[0] is '#':
        return False

    return parseBase(line)


def parseDecimal(line):
    for digit in line:
        if digit not in '0123456789':
            return False
    return True


def parseBase(line):
    possibleDigits = '0123456789abcdef'
    if line.split('#')[2] is not '':
        return False
    base = int(line.split('#')[0])
    num = line.split('#')[1]
    if num is '':
        return False
    if base < 2 or base > 16:
        return False
    for digit in num:
        if digit not in possibleDigits[0:base]:
            return False
    return True


print("123_456_789=", adaNumber("123_456_789"))  # true
print("16#123abc#=", adaNumber("16#123abc#"))  # true
print("10#123abc#=", adaNumber("10#123abc#"))  # false
print("10#10#123ABC#9=", adaNumber("10#10#123ABC#"))  # false
print("10#0#=", adaNumber("10#0#"))  # true
print("10##=", adaNumber("10##"))  # false
print("16#1234567890ABCDEFabcdef#=", adaNumber("16#1234567890ABCDEFabcdef#"))  # true
print("1600#=", adaNumber("1600#"))   # false
print("7#???#=", adaNumber("7#???#"))  # false
print("4#4#=", adaNumber("4#4#"))  # false
print("3454235ab534=", adaNumber("3454235ab534"))  # false
print("1#0#=", adaNumber("1#0#"))  # false
print("1_#0_#=", adaNumber("1_#0_#"))  # false
print("17#ac#=", adaNumber("17#ac#"))  # false
print("2#10110#=", adaNumber("2#10110#"))  # true
print("2#10110=", adaNumber("2#10110"))  # false
print("#2#10110=", adaNumber("#2#10110"))  # false
print("#2#10110#=", adaNumber("#2#10110#"))  # false
print("9##=", adaNumber("9##"))  # false


'''def adaNumber(line):
    line = line.replace('_', '')
    if line.isdigit():
        return True
    try:
        b, n = line.split('#')[:-1]
        if int(b) < 2 or int(b) > 16:
            return False
        try:
            int(n, int(b))
            return True
        except ValueError:
            return False
    except ValueError:
        return False
'''

'''def adaNumber(line):
    line = line.replace("_", "")
    if "#" not in line:
        try:
            int(line)
        except:
            return False
    else:
        try:
            n = int(line[line.find("#") + 1:line.rfind("#")], int(line[:line.find("#")]))
            if int(line[:line.find("#")]) > 16 or int(line[:line.find("#")]) < 2:
                return False
        except:
            return False
    return True
'''
