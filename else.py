number=int(input("enter a number:"))
if(number<=0):
    print("enter a positive number")
else:
    i=1
    while(i!=10):
        print(f"{number}*{i}=",number*i)
        i=i+1              
    