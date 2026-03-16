#4. WAP to check whether the given value's last digit is greater than 5 or 
#not.if greater,
a=int(input("enter the num:"))
if(a%10>=5):
    b=a>>2
    print(f"{a} right shif{b}")
else:
    print("it does not end with 5")    