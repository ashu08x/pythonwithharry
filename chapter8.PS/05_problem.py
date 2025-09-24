'''
#same result as below find the difference if exist
def pattern(n):
    if(n==0):
        return 
    print("*" * n)
    return pattern(n-1)
pattern(5)
'''


def pattern(n):
    if(n==0):
        return 
    print("*" * n)
    pattern(n-1)
pattern(5)