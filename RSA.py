import maths
 

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
    return e #func returning the value

   Euclid's Algorithm
def eugcd(e,r):
    for i in range(1,r):
        while(e!=0):
            a,b=r//e,r%e
            if(b!=0):
                print("")
#                 print("{} = {}x{} + {}".format(r,a,e,b))
            r=e
            e=b
