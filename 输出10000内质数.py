def isprime(i):
    for m in range(3,int(i/3)+1,1):
        if i%m==0:
            return False
        else:
            pass
    return True
print(2,3)
for k in range(5,10000,2):
    if isprime(k):
        print(k)
    else:
        pass
input("\n\nPress enter to exit")
