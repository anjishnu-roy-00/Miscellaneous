def majority_element_naive(elements):
    d={}
    s = set(elements)
    for elem in s:
        d[elem]=1
    surpass = len(elements)
    for elem in elements:
        if d[elem]>(surpass//2):
            return 1
        d[elem]+=1       
    return 0

nums = [2]
res = majority_element_naive(nums)
print(res)
