a=int(input("Enter number 1:"))
b=int(input("enter number 2:"))
op=input("Enter ypur required operation:")
if op=='+':
    print("result:"+str(a+b))
elif op=='-':
    print("result:"+str(a-b))
elif op=='*':
    print("result:"+str(a*b))
elif op=='/':
    print("result:"+str(a/b))
elif op=='//':
    print("result:"+str(a//b))
elif op=='%':
    print("result:"+str(a%b))
else:
    print("Enter valid sign")
