def one_dart_names():
    one_dart = {}
    for i in range(1, 21):
        one_dart[i] = 'single ' + str(i)
        if i*2 not in range(1, 21):
            one_dart[i*2] = 'double ' + str(i)
        if i*3 not in range(1, 21) and i*3 not in range(2, 42, 2):
            one_dart[i*3] = 'triple ' + str(i)
    one_dart[25] = 'single bull'
    one_dart[50] = 'double bull'
    return(one_dart)


def one_dart_list():
    one_dart = [0]
    for i in range(1, 21):
        one_dart.append(i)
        if i*2 not in range(1, 21):
            one_dart.append(i*2)
        if i*3 not in range(1, 21) and i*3 not in range(2, 42, 2):
            one_dart.append(i*3)
    one_dart.append(25)
    one_dart.append(50)
    return(sorted(one_dart))


def two_dart_dict():
    one_dart = one_dart_list()
    two_dart_combos = {}
    for i in range(len(one_dart)):
        for j in range(i, len(one_dart)):
            micro = []
            micro.append(one_dart[i])
            micro.append(one_dart[j])
            if sum(micro) in two_dart_combos and micro not in two_dart_combos[sum(micro)]:
                two_dart_combos[sum(micro)].append(micro)
            else:
                two_dart_combos[sum(micro)] = [micro]
    return(two_dart_combos)


def three_dart_dict():
    one_dart = one_dart_list()
    three_dart_combos = {}
    for i in range(len(one_dart)):
        for j in range(i, len(one_dart)):
            for k in range(j, len(one_dart)):
                micro = []
                micro.append(one_dart[i])
                micro.append(one_dart[j])
                micro.append(one_dart[k])
                if sum(micro) in three_dart_combos and micro not in three_dart_combos[sum(micro)]:
                    three_dart_combos[sum(micro)].append(micro)
                else:
                    three_dart_combos[sum(micro)] = [micro]
    return(three_dart_combos)


'''
twos = three_dart_dict()
dart = one_dart_names()

for x in twos[64][0]:
    if x in dart:
        print(dart[x])'''

# print(len(macro[12]))
'''y = {x: len(two_dart_combos[x]) for x in two_dart_combos}
for i in y:
    print(i, y[i])'''
