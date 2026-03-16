a=eval(input("enter the value:"))
if(type(a) in [str,list,tuple,set,dict]):
    b=tuple(a)
    print(f"b:{b} b's class is{type(b)},a's class is{type(a)}")
else:
    print("it is not svd")    