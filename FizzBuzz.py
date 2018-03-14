#! python2
# supposed to make force python2 use, doesn't work in atom
import sys
print(sys.executable)
print(sys.version)

for i in range(0, 100):
    output = ""

    if(i % 2 == 0):
        output += 'Even'
    if(i % 3 == 0):
        output += 'Fizz'
    if(i % 5 == 0):
        output += 'Buzz'
    if(i % 7 == 0):
        output += 'Sevr'
    if(output == ''):
        output = i

    print(output)
