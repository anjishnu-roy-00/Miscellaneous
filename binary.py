def binary_search(keys,query):
    mid = 0
    left = 0
    right = len(keys)-1
    while right >= left:
        mid = (left+right)//2
        if query == keys[mid]:
            return mid
        if query < keys[mid]:
            right = mid - 1
        if query > keys[mid]:
            left = mid + 1
    return -1

query = [8,1,23,1,11,13]
keys = [1,5,8,8,8,12,13]
for elem in query:
    print(binary_search(keys,elem))
