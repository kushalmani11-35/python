a=input("enter the character")
if(a in "aeiouAEIOU"):
    b=chr(ord(a)+1)
    print(f"the next vowel is{b}")
else:
    print("it is not a vowel:")
