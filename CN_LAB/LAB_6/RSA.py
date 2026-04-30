import math
p=int(input("Enter 1st Prime:"))
q=int(input("Enter 2nd Prime:"))
n=p*q
phai=(p-1)*(q-1)
e=7

#gcd check
if math.gcd(e,phai)!=1:
    print("Invalid")
else:
    d=1
    while(d*e) % phai !=1:
        d=d+1
    print("Public key",e,n)
    print("Private Key",d,n)

    msg=int(input("Enter the original message:"))
    print("Org msg",msg)
    enctp=(msg**e)%n
    print("Encryptived message is:",enctp)
    dypt=(enctp**d)%n
    print("Decrypted message is:",dypt)
