#wap to find the given num is even or not by using bitwise 
a=int(input("enter the number :"))
if(a&1==0):
    print(a)
else:
    print('not')