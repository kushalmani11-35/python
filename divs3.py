#checking the number is a amstrong number or not
def luffy():
    a=int(input("enter the number"))
    b=a
    f=a
    c=0
    t=0
    while(a>0):
        ld=a%10
        c=c+1
        a=a//10
    while(b>0): 
        n=b%10
        d=n**c
        t+=d
        b=b//10
    if(f==t):
        print("it is a amstrong number")
    else:
        print("it is not a amstrong number")
luffy()                