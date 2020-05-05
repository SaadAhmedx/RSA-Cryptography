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
 
#Multiplicative Inverse
def mult_inv(e,r):
    gcd,s,_=eea(e,r)
    if(gcd!=1):
        return None
    else:
#         if(s<0):
#             print("")           
# #             print("s=%d. Since %d is less than 0, s = s(modr), i.e., s=%d."%(s,s,s%r))
#         elif(s>0):
#             print("")                
# #             print("s=%d."%(s))
        return s%r
 
#e Value Calculation
'''FINDS THE HIGHEST POSSIBLE VALUE OF 'e' BETWEEN 1 and 1000 THAT MAKES (e,r) COPRIME.'''
for i in range(1,1000):
    if(egcd(i,r)==1):
        e=i
# print("The value of e is:",e)
# print("*****************************************************")
 
#d, Private and Public Keys
'''CALCULATION OF 'd', PRIVATE KEY, AND PUBLIC KEY.'''
# print("EUCLID'S ALGORITHM:")
eugcd(e,r)
# print("END OF THE STEPS USED TO ACHIEVE EUCLID'S ALGORITHM.")
# print("*****************************************************")
# print("EUCLID'S EXTENDED ALGORITHM:")
d = mult_inv(e,r)
# print("END OF THE STEPS USED TO ACHIEVE THE VALUE OF 'd'.")
# print("The value of d is:",d)
# print("*****************************************************")
public = (e,n)
private = (d,n)
# print("Private Key is:",private)
# print("Public Key is:",public)
# print("*****************************************************")
 
#Encryption
'''ENCRYPTION ALGORITHM.'''
def encrypt(pub_key,n_text):
    e,n=pub_key
    x=[]
    m=0
    for i in n_text:
        if(i.isupper()):
            m = ord(i)-65
            c=(m**e)%n
            x.append(c)
        elif(i.islower()):               
            m= ord(i)-97
            c=(m**e)%n
            x.append(c)
        elif(i.isspace()):
            spc=400
            x.append(400)
    return x
     
 
#Decryption
'''DECRYPTION ALGORITHM'''
def decrypt(priv_key,c_text):
    d,n=priv_key
    txt=c_text.split(',')
    x=''
    m=0
    for i in txt:
        if(i=='400'):
            x+=' '
        else:
            m=(int(i)**d)%n
            m+=65
            c=chr(m)
            x+=c
    return x
 
#Message
print("RSA ENCRYPTOR/DECRYPTOR")
while True:
    message = input("Enter Message:")
    
    if message != "N":
        choose = input("1. FOR ENCRYPTION\n2. FOR DECRYPTION\n")
        if(choose=='1'):
            
            print("{}\nYour encrypted message is: {}\n{}".format('*'*26, encrypt(public,message), '*'*26))
        elif(choose=='2'):
            print("{}\nYour decrypted message is: {}\n{}".format('*'*26, decrypt(private,message).replace(" ", " ").lower(), '*'*26))
        else:
            print("You entered the wrong option.")

    else:
        print(";)")
        break;
