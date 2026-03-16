#18. WAP to check whether a given value is a negative or even number. 
#If satisfied ,to 
#display the last digit of the values. 
a=int(input("enter the num:"))
if(a<0 or a%2==0):
    b=abs(a)%10
    print("last value of num is :",b)
    