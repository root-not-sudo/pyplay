def areSimilar(a, b):
    if(a == b):
        return(a == b)
    else:
        index1, index2, falseTracker = -1, -1, 0
        for i in range(len(a)):
            if (not a[i] == b[i]):
                falseTracker += 1
                if(index1 == -1):
                    index1 = i
                else:
                    index2 = i
            if falseTracker > 2:
                return False
        return(a[index1] == b[index2] and a[index2] == b[index1])


print('test 1 =', areSimilar([1, 2, 3], [1, 2, 3]))
print('test 2 =', areSimilar([1, 2, 3], [2, 1, 3]))
print('test 3 =', areSimilar([1, 2, 2], [2, 1, 1]))
print('test 4 =', areSimilar([1, 1, 4], [1, 2, 3]))
print('test 5 =', areSimilar([1, 2, 3], [1, 10, 2]))
print('test 6 =', areSimilar([2, 3, 1], [1, 3, 2]))
print('test 7 =', areSimilar([2, 3, 9], [10, 3, 2]))
print('test 8 =', areSimilar([4, 6, 3], [3, 4, 6]))
print('test 9 =', areSimilar([832, 998, 148, 570, 533, 561, 894, 147,
                              455, 279], [832, 998, 148, 570, 533, 561, 455, 147, 894, 279]))
print('test 10 =', areSimilar([832, 998, 148, 570, 533, 561, 894, 147,
                               455, 279], [832, 570, 148, 998, 533, 561, 455, 147, 894, 279]))
