a=int(input("enter a first number:"))
b=int(input("enter a second number:"))
c=int(input("enter a third number:"))

if(a>b and a>c):
    print(f"{a} is largest number")
if(b>a and b>c):
    print(f"{b} is largest number")
if(c>a and c>b):
    print(f"{c} is largest number")
else:
    print(f"{c} is largest number ")