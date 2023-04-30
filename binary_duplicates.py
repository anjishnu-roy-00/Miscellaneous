def binary_search(keys,query):
    mid = 0
    seek = len(keys)
    flag = 0
    left = 0
    right = len(keys)-1
    while right >= left:
        mid = (left+right)//2
        if query == keys[mid] and mid<seek:
            flag = 1
            seek = mid
            right = mid - 1
        if query < keys[mid]:
            right = mid - 1
        if query > keys[mid]:
            left = mid + 1
    if flag == 1:
        return seek
    return -1

query = [8,1,23,1,11,13]
keys = [1,5,8,8,8,8,12,13]
for elem in query:
    print(binary_search(keys,elem))
