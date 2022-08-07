'''
Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]
'''

def unique_in_order(iterable):
    lst = []
    n = 0
    for i in range(len(iterable)):
        alpha = iterable[i]
        if i == 0:
            lst.append(alpha)
            n += 1
        elif lst[n-1] != alpha:
            lst.append(alpha)
            n += 1
        else:
            pass
    return lst