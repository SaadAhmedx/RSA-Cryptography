
import math
p = 193
q = 197
def prime_check(a):
    if(a==2):
        return True
    elif((a<2) or ((a%2)==0)):
        return False
    elif(a>2):
        for i in range(2,a):
            if not(a%i):
                return false
    return True
#RSA Modulus
n = p * q
#Eulers Toitent
r= (p-1)*(q-1)
#GCD
def egcd(e,r):
    while(r!=0):
        e,r=r,e%r
    return e
```
