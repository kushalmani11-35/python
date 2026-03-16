a=eval(input("enter the value:"))
if(type(a) in [str,tuple,int,float,complex,bool]):
    b=set(a)
    print(f"b:{b} b's class is{type(b)},a's class is{type(a)}")
else:
    print("it is not imu")    