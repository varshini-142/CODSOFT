a=int(input("Enter number 1:"))
b=int(input("enter number 2:"))
op=input("Enter your required operation:")
if op=='+':
    print("result:"+str(a+b))
elif op=='-':
    print("result:"+str(a-b))
elif op=='*':
    print("result:"+str(a*b))
elif op=='%':
    print("result:"+str(a%b))
elif op=='//':
    print("result:"+str(a//b))
elif op=='/':
    if(b!=0):
        print("result:"+str(a/b))
    else:
        print("Number is not divisible by 0")
else:
    print("Enter valid sign")
