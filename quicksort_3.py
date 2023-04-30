'''
This quicksort algorithm uses a three way split
one part contains all elements smaller than the randomly chosen pivot
one part contains all elements larger than the randomly chosen pivot
the third part contains elements that are equal to the pivot
In traditional quicksort algorithms we mostly implement a two way split(small|large)
The three way split reduces runtime greatly when considering duplicate elements
'''
from random import randint


def partition3(array, left, right):
    # write your code here
    x = array[left]
    lt = left
    i = left
    gt = right
    pivot = array[left]
    while i <= gt:
        if array[i] < pivot:
            array[lt],array[i]=array[i],array[lt]
            lt+=1
            i+=1
        elif array[i] > pivot:
            array[i],array[gt] = array[gt],array[i]
            gt-=1
        else:
            i+=1
    
    return lt,gt

def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    m1, m2 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m2 + 1, right)


L = [2911,11,895,65,123,123,123,44,-200,1234,5400,2390,-2390,2390]
randomized_quick_sort(L,0,len(L)-1)
print(*L)