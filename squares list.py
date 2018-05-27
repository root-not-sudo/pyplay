'''for i in range(1, 316228):
    print(i, '=', i * i)'''

str = '90039'
c = []
for i in range(len(str)):
    if str[i] not in str[0:i]:
        c.append(str.count(str[i]))

c.sort()
print(c)
