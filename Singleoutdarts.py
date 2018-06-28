#import console


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


def input_throw(score):
    while True:
        try:
            hit = int(input('What did you hit? '))
            if hit not in one_dart_list():
                raise ValueError
            else:
                score -= hit
                break
        except ValueError:
            print('Please enter a valid number')
    if score > 0:
        print('You are at', score)
    return(score)


def main():
    # console.clear()
    threes = three_dart_dict()
    twos = two_dart_dict()
    ones = one_dart_list()
    dart_dict = one_dart_names()
    while True:
        try:
            start_score = int(input('What is your score? '))
            score = start_score
            break
        except ValueError:
            print('Please enter a valid number')
    if score not in threes:
        print('Sorry, it can\'t be done with 3 darts')
    else:
        for i in threes[score][0]:
            if i in dart_dict:
                print(dart_dict[i])
    if score > 0:
        score = input_throw(score)
        if score not in twos and score > 0:
            print('Sorry, it can\'t be done with 2 darts')
        elif score > 0:
            for i in twos[score][0]:
                if i in dart_dict:
                    print(dart_dict[i])

    if score > 0:
        score = input_throw(score)
        if score not in ones and score > 0:
            print('Sorry, it can\'t be done with 1 dart')
        elif score > 0:
            print(dart_dict[score])

    if score > 0:
        score = input_throw(score)

    if score < 0:
        print('Busted :-/')
        score = start_score
    if score in threes and score > 0:
        print('Next time try:')
        for i in threes[score][0]:
            if i in dart_dict:
                print(dart_dict[i])
    if score == 0:
        print('You win!')


while True:
    main()
    clear = input("")
