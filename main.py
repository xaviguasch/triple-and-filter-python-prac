'''
triple_and_filter([1,2,3,4]) # [12]
triple_and_filter([6,8,10,12]) # [24,36]
'''


def triple_and_filter(collection):
    return list(filter(lambda x: x % 4 == 0, map(lambda x: x * 3, collection)))


print(triple_and_filter([6,8,10,12]))

