import maths # adding library
 

p = 193  # intializing variable
q = 197  # initializing variable

n = p * q # product of 2 numbers
print("RSA Modulus: {}".format(n)) #print n in format of RSA modulus

#Eulers Toitent

r = (p-1)*(q-1)
print("Eulers Toitent: {}".format(r))

def egcd(e,r):   #method define
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
    if(gcd!=1):           #checking conditon 
    return None
    else:  
 #    if(s<0):            #checking conditon 
 #    print("")   
# #   print("s=%d. Since %d is less than 0, s = s(modr), i.e., s=%d."%(s,s,s%r))
for i in range(1,1000):
 if(egcd(i,r)==1):            #checking conditon 
        e=i
   print("The value of e is:",e)
print("*****************************************************")
Private and Public Keys
'''CALCULATION OF 'd', PRIVATE KEY, AND PUBLIC KEY.'''
 print("EUCLID'S ALGORITHM:")
eugcd(e,r)
def egcd(e,r):
  while(r!=0):
   e,r=r,e%r
  return e
#Euclid's Algorithm
def eugcd(e,r):
  for i in range(1,r):
        while(e!=0):
            a,b=r//e,r%e
      if(b!=0):
                print("")
#                 print("{} = {}x{} + {}".format(r,a,e,b))
            r=e
            e=b
  #Extended Euclidean Algorithm
  def eea(a,b):
    if(a%b==0):
        return(b,0,1)
    else:
        gcd,s,t = eea(b,a%b)
        s = s-((a//b) * t)
       #         print("%d = %d*(%d) + (%d)*(%d)"%(gcd,a,t,s,b))
        return(gcd,t,s)
public = (e,n)
private = (d,n)
print("Private Key is:",private)
print("Public Key is:",public)
d = mult_inv(e,r)
print("END OF THE STEPS USED TO ACHIEVE THE VALUE OF 'd'..")
print("The value of d is:",d)
print("***************************************************")
public = (e,n)
private = (d,n)
print("Private Key is:",private)
print("Public Key is:",public)
print("***************************************************")
#Decryption
'''DECRYPTION ALGORITHM'''
def decrypt(priv_key,c_text):
    d,n=priv_key
    txt=c_text.split(',')
    x=''
m=0
    for i in txt:
        if(i=='400'): #condition
            x+=' '
        else:
 m=(int(i)**d)%n 
            m+=65
            c=chr(m)
            x+=c
    return x
#Message
message = input("What would you like encrypted or decrypted?(Separate numbers with ',' for decryption):")
print("Your message is:",message)
#Choose Encrypt or Decrypt and Print
choose = input("Type '1' for encryption and '2' for decrytion.")
if(choose=='1'):  #checking condition
 enc_msg=encrypt(public,message)
    print("Your encrypted message is:",enc_msg)
    print("Thank you for using the RSA Encryptor. Goodbye!")
elif(choose=='2'): #else if condition check
print("Your decrypted message is:",decrypt(private,message))
    print("Thank you for using the RSA Encryptor. Goodbye!")
else:
 print("You entered the wrong option.")
    print("Thank you for using the RSA Encryptor. Goodbye!")



