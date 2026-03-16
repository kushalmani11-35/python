a=input("enter the value:")
if('A'<= a<='Z'):
    b=chr(ord(a)+32)
    c={b:ord(b)}
    print(c)
else:
    print("it is not a upper case")    
