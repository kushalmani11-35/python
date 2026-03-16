#5. WAP to check whether a given input is divisible by 3 or 5. If the condition is satisfied, the number is converted to a list. i/p: 30 o/p:[‘3’,’0’] 
a=input("enter the num:")
if(int(a)%3==0 or int(a)%5==0):
    b=list[a]

    print(f"list of {a} is {b}")
else:
    print(f"{a}is not divisable by 5 and 3")    