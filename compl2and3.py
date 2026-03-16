#4. WAP to check whether given input is divisible by 2 and 6. If the condition is satisfied, convert the given number into a complex number
a=int(input("enter the num:"))
if(a%2==0 and a%6==0):
    b=complex(a)
    print(f"complex of {a} is {b}")
else:
    print(f"{a}is not divisable by 2 and 3")    

    