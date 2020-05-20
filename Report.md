# DM 103347: RSA Cryptography #
<!-- Replace XX with your course ID-->
### PROJECT MEMBERS ###
StdID | Name
------------ | -------------
**62499** | **Saad Ahmed** <!--this is the group leader in bold-->
63152 | Syed Muhammad Mohtashim Kamal
63687 | Ayesha Aamir 
63008 | Muhammad Rafay
63341 | Ghanwa Batool 
<!-- Replace name and student ids with acutally group member names and ids-->
## Project Description ##
This program is an implementation of the famous RSA Algorithm in PYTHON. In this project we have used Euler’s Totient, Euclid's Algorithm, GCD for checking prime numbers, multiplicative inverse, encryption, and decryption. It was required to know and understand every step of the algorithm in a detailed manner. We learned to put together different functions, convert them from a mathematical perspective to a programmer perspective, and produce a completely different output.

## Discrete Math Concepts Used ##
We have used different **Discrete Mathematics** concepts in our program, amongst them some of the most important one's are: Multiplicative Inverse, Euler’s Totient, Euclid's Algorithm and GCD for checking prime numbers. As We all know RSA algorithm purely works on Prime numbers to generate keys. So all the mentioned concepts are used to make program workable.

### Example 1: Check Prime ###
''' This is simple function that check the value of p,q if the values are PRIME OR NOT '''
```def prime_check(a):
    if(a==2):
        return True
    elif((a<2) or ((a%2)==0)):
        return False
    elif(a>2):
        for i in range(2,a):
            if not(a%i):
                return false
    return True
```

### Example 2: Euclid's Algorithm ### 
'''Euclid's Algorithm Code will take to paramter e,r,  run loop to the range of r & assigning  Floor division value to a & Modulus to b '''
```def eugcd(e,r):
    for i in range(1,r):
        while(e!=0):
            a,b=r//e,r%e
            if(b!=0):
                print("")
            r=e
 ```       
### Example 3: Encryption ###

''' In ENCRYPTION ALGORITHM the encrypt function simple take our input as parameter encrypt the msg & stored in the array'''
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


```
## Problems Faced ##
We didn't really face much problems while making this program as we all have worked on PYTHON before and all the concepts which are used in our program were well explained in classes but the only thing which we found a bit difficult was using the different concepts/algorithms in one program. We first designed each algorithm and function separately then while combining them into one to make our program work was a quite complicated task but by the dedication of all members we solved everything perfectly as now you can see we have flawless and smooth running program.

## References ##
- Euler’s Totient https://www.youtube.com/watch?v=qa_hksAzpSg
- GCD https://www.youtube.com/watch?v=cahuG1cEQdY
- RSA Algorithm https://www.geeksforgeeks.org/rsa-algorithm-cryptography/
