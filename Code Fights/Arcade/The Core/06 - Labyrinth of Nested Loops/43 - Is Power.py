from math import log, floor, sqrt, ceil


def isPower(n):

    if n == 1:
        return True
    for i in range(2, floor(sqrt(n))+1):
        whole_number = log(n)/log(i)
        if whole_number - floor(whole_number) < 10e-12 or abs(ceil(whole_number) - whole_number) < 10e-12:
            return True
    return False


print(isPower(243))

myfunctionlist = []
for i in range(1, 401):
    if isPower(i):
        myfunctionlist.append(i)
print(myfunctionlist)

totalpowers = [1]
for i in range(2, 21):
    for j in range(2, 10):
        if i ** j <= 400 and i ** j not in totalpowers:
            totalpowers.append(i ** j)
print(sorted(totalpowers))
