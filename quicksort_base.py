'''
Standard quicksort algorithm with random pivot element and 2 partitions
'''

from random import randint

def partition(array, left, right):
    # write your code here
    x = array[left]
    j = left
    for i in range(left+1,right+1):
        if array[i]<=x:
            j+=1
            array[j],array[i] = array[i],array[j]
    array[left],array[j] = array[j],array[left]
    return j


def randomized_quick_sort(array, left, right):
    if left >= right:
        return 
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    m = partition(array, left, right)
    randomized_quick_sort(array, left, m - 1)
    randomized_quick_sort(array, m + 1, right)



L = [2911,11,895,65,123,123,123,44,-200,1234,5400,2390,-2390,2390]
randomized_quick_sort(L,0,len(L)-1)
print(*L)