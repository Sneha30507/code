def add(x,y):
    return x+y
def subtarct(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
print("Select opertion.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice=input("Enter choice(1/2/3/4):")

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))

if choice=='1':
    print(num1,"+",num2,"=",add(num1,num2))
elif choice=='2':
    print(num1,"-",num2,"=",subtarct(num1,num2))
elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid Input")
