import maths # adding library
 

p = 193  # intializing variable
q = 197  # initializing variable

 
#RSA Modulus

n = p * q # product of 2 numbers
print("RSA Modulus: {}".format(n)) #print n in format of RSA modulus

#Eulers Toitent

r = (p-1)*(q-1)
print("Eulers Toitent: {}".format(r))

def egcd(e,r):    # method defined
    while(r!=0): #checking condition
        e,r=r,e%r
    return e #function returning the value

   def eugcd(e,r):          #defining function for gcd
    for i in range(1,r):    # for loop applied for euler process
        while(e!=0):        # while loop condition
            a,b=r//e,r%e    # mathematical process
            if(b!=0):       # checking condition
                print("")
            r=e             # swapping process
            e=b
#                 print("{} = {}x{} + {}".format(r,a,e,b))
#Multiplicative Inverse
def mult_inv(e,r):         # method define(mutltiplicative inverse)
 gcd,s,_=eea(e,r)
    if(gcd!=1):            
    return None
    else:  
 #    if(s<0):
 #    print("")   
# #   print("s=%d. Since %d is less than 0, s = s(modr), i.e., s=%d."%(s,s,s%r))
for i in range(1,1000):
 if(egcd(i,r)==1):
        e=i
   print("The value of e is:",e)
print("*****************************************************")
Private and Public Keys
'''CALCULATION OF 'd', PRIVATE KEY, AND PUBLIC KEY.'''
 print("EUCLID'S ALGORITHM:")
eugcd(e,r)
