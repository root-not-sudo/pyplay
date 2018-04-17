# -*- coding: utf-8 -*-


def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)


def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))


def Towers(n, fr, to, spare):
    if n == 1:
        print(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)


def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)


def isPalindrome(s):
    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChars(s))


def fib_efficent(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib_efficent(n-1, d) + fib_efficent(n-2, d)
        d[n] = ans
        return ans


d = {1: 1, 2: 2}

print(fib_efficent(1, d))
