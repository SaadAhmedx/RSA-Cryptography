
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
            r=e
            e=b
 
#Extended Euclidean Algorithm
def eea(a,b):
    if(a%b==0):
        return(b,0,1)
    else:
        gcd,s,t = eea(b,a%b)
        s = s-((a//b) * t)
        return(gcd,t,s)

#Multiplicative Inverse
def mult_inv(e,r):
    gcd,s,_=eea(e,r)
    if(gcd!=1):
        return None
    else:
        print("")                
        return s%r
    
'''FINDS THE HIGHEST POSSIBLE VALUE OF 'e' BETWEEN 1 and 1000 THAT MAKES (e,r) COPRIME.'''
for i in range(1,1000):
    if(egcd(i,r)==1):
        e=i
eugcd(e,r)
d = mult_inv(e,r)
public = (e,n)
private = (d,n)

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
    try:
        for i in txt:
            if(i=='400'):
                x+=' '
            else:
                m=(int(i)**d)%n
                m+=65
                c=chr(m)
                x+=c

        return x
    
    except:
        print("Oopss Invalid Encrypted Message")
        sys.exit(1)

Message = "[~]WELCOME TO RSA ENCRYPTOR/DECRYPTOR[~]\n"
byeMessage = "\n\n[~]THANKS FOR USING RSA ENCRYPTOR/DECRYPTOR[~]"
for i in range(len(Message)):
    print(Message[i], end="")
    time.sleep(0.1)

