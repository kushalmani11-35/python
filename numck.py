#12. WAP to take the input from the user as a number and check whether 
#it is a number 
#or not. if yes. take the number and add some value and print it. 
a=eval(input("enter the char:"))
if(type(a) in [int,float,complex]):
    print(f"it is a num and 5 is added to {a} is {a+5}")
else:
    print("it is not a num")    