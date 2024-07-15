def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    if(y==0):
        print("2nd number can't ve zero.")
    else:
        return x/y

num1=float(input("Enter first num:"))
num2=float(input("Enter second num:"))

print("\n1.Addition")
print("\n2.Subtraction")
print("\n3.Multiplication")
print("\n4.Division")
print("\n5.Exit")

choice = int(input("\nEnter your choice only from 1-5:"))

if(choice==1):
    print("Addition of those nos. are :",add(num1,num2))
elif(choice==2):
    print("Subtraction of those nos. are:",sub(num1,num2))
elif(choice==3):
    print("Multiplication of those nos. are:",mul(num1,num2))
elif(choice==4):
    print("Division of those nos. are:",div(num1,num2))
elif(choice==5):
    print("Thank you for using the calculator. Goodbye!")
else:
    print("Enter the CORRECT choice.")
