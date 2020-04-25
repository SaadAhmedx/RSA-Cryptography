import math
 

#Hardcoded Prime Number

p = 193
q = 197

 
#RSA Modulus

n = p * q
print("RSA Modulus: {}".format(n))

#Eulers Toitent

r = (p-1)*(q-1)
print("Eulers Toitent: {}".format(r))