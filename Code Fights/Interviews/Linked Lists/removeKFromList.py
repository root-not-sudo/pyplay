# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#


def removeKFromList(l, k):
    a = []
    while l != None:
        if l.value != k:
            a.append(l.value)
        l = l.next
    return a


print(removeKFromList([3, 1, 2, 3, 4, 5], 3))
