def makeArrayConsecutive2(statues):

    statues.sort()
    print(statues)
    count = 0
    for i in range(len(statues)-1):
        j = statues[i]
        while j+1 < statues[i + 1]:
            count += 1
            j += 1
    return count


# smarter:
'''def makeArrayConsecutive2(statues):
    return max(statues)-min(statues)-len(statues)+1'''
