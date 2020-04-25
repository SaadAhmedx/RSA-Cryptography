import maths # adding library
 

p = 193  # intializing variable
q = 197  # initializing variable

 
#RSA Modulus

n = p * q # product of 2 numbers
print("RSA Modulus: {}".format(n))

#Eulers Toitent

r = (p-1)*(q-1)
print("Eulers Toitent: {}".format(r))

def egcd(e,r):
    while(r!=0):
        e,r=r,e%r
    return e #function returning the value

   def eugcd(e,r):
    for i in range(1,r):
        while(e!=0):
            a,b=r//e,r%e
            if(b!=0):
                print("")
#                 print("{} = {}x{} + {}".format(r,a,e,b))
#Multiplicative Inverse
def mult_inv(e,r):
            r=e
            e=b
