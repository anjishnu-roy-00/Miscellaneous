'''
This is the algorithm for calculating GCD using Eucledian method
We learned it in school as the division method(?)
'''
def gcd(a,b):
    if b==0:
        return a
    r = a%b
    a = b
    b = r
    return gcd(a,b)
res = gcd(3918848,1653264)
print(res)
    
