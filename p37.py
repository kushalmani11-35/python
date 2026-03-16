a=input("enter the character")
if(a not in "aeiouAEIOU"):
    b=chr(ord(a)-1)
    print(f"the not a vowel is{b}")
else:
    print("it is  vowel:")
