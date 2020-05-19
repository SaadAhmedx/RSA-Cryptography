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
We have used different discrete Mathematics conscepts in our program, amongs them some of the most important one's are: Multiplicative Inverse, Euler’s Totient, Euclid's Algorithm and GCD for checking prime numbers. As We all know RSA algorithm purely works on Prime numbers to generate keys. So all the mentioned concepts are used to make program workable.
### Example 1: Multiplicative Inverse ###
```def mult_inv(e,r):
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
```
### Example 2: GCD ###
```def egcd(e,r):
    while(r!=0):
        e,r=r,e%r
    return e
```
### Example 3: Euclid's Algorithm ### 
```def eugcd(e,r):
    for i in range(1,r):
        while(e!=0):
            a,b=r//e,r%e
            if(b!=0):
                print("")
#                 print("{} = {}x{} + {}".format(r,a,e,b))
            r=e
            e=b
```
## Problems Faced ##
Replace this text with the explaination of the problems you faced in the project, and how you resolved them. Again you can give each of your problems a heading of level 3.

### Problem 1: I don't know how to Code ###
Transfer to yourself to social sciences department. Blah blah blah. This is an example. Replace it with your own problem description and how you resolved it. 
Don't just blindly copy paste this report. This is a sample template file. 

### Problem 2: My Parents forced me for a degree ###
If you were not able to convince your parents not to force you for degree and now you are doing it for them then do it with your best effort and not half heartedly. There is no point wasting this time with finding a loop hole here and there and passing courses without actually learning anything.  

## References ##
- Euler’s Totient https://www.youtube.com/watch?v=qa_hksAzpSg
- GCD https://www.youtube.com/watch?v=cahuG1cEQdY
- RSA Algorithm https://www.geeksforgeeks.org/rsa-algorithm-cryptography/
