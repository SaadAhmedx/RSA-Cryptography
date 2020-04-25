import maths
 

p = 193
q = 197


n = p * q # product of 2 numbers
print("RSA Modulus: {}".format(n))

#Eulers Toitent

r = (p-1)*(q-1)
print("Eulers Toitent: {}".format(r))

def egcd(e,r):
    while(r!=0):
        e,r=r,e%r
    return e #function returning the value
