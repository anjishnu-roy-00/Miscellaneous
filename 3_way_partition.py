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


L = [2911,11,895,65,123,123,123,44,-200,1234,5400,2390,-2390,2390]
x,y = partition3(L,0,len(L)-1)
print(len(L),x,y)