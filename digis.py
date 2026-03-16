'''a=abs(int(input("enter the number :")))
if(100<=a<=999 or-100<=a<=-999):
    print(f"{a}is a 3 digits")
else:
    print("no its not a 3 digits num")    '''
def fact(n):
    if n==1 or n==0:
        return 1
    return n*fact(n-1)
print(fact(5))