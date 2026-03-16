#4. WAP to check whether the given value's last digit is greater than 5 or 
#not.if greater,
a=int(input("enter the num:"))
if(a%3==0 and a>=30):
    b=a**2
    print(f"{a} square is{b}")
else:
    print("it valu is less tha 30")    