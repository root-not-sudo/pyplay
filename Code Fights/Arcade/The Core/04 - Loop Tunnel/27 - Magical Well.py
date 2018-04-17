def magicalWell(a, b, n):
    money = 0
    for i in range(n):
        money += a * b
        a, b = a+1, b+1
    return money


# recursive:
'''def magicalWell(a, b, n):
    if not n:
        return 0

    return a*b + magicalWell(a+1,b+1,n-1)'''

# return sum:
'''def magicalWell(a, b, n):
    return sum((a+i)*(b+i) for i in range(n))'''


print(magicalWell(1, 2, 2))
