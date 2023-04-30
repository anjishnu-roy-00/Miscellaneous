# Discrete Knapsack problem without repetition

import numpy 

def partitions(W, n, items):
    """ Finds if number of partitions having capacity W is >=3
    (int, int, list) -> (int) """
    count = 0
    print(n)
    print(W)
    print(items)
    value = numpy.zeros((W+1, n+1))
    for i in range(1, W+1):
        for j in range(1, n+1):
            value[i][j] = value[i][j-1]
            if items[j-1]<=i:
                temp = value[i-items[j-1]][j-1] + items[j-1]
                if temp > value[i][j]:
                    value[i][j] = temp
            if value[i][j] == W: count += 1
    print(value)
    if count < 3: print('0')
    else: print('1')

if __name__ == '__main__':
    n = 13
    item_weights = [1,2,3,4,5,5,7,7,8,10,12,19,25]
    total_weight = sum(item_weights)
    if n<3: 
        print('0')
    elif total_weight%3 != 0: 
        print('0')
    else:
        partitions(total_weight//3, n, item_weights)
