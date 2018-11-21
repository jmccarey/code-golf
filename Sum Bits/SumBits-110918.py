def invRootSum(s):
    a=0
    for n in''.join(format(ord(x),'b')for x in s):a+=int(n)
    return a**-.5
    

s= "q"
print(invRootSum(s))