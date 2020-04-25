import math
 

#Hardcoded Prime Number

p = 193
q = 197

 
#RSA Modulus

n = p * q # product of 2 numbers
print("RSA Modulus: {}".format(n))

#Eulers Toitent

r = (p-1)*(q-1)
print("Eulers Toitent: {}".format(r))

def egcd(e,r):
    while(r!=0):
        e,r=r,e%r
    return e
