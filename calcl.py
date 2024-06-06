running=True
while running:
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    c=input("Enter the symbol: ")

    if c == "+":
        print("The sum of a+b is ",a+b)
    elif c =="-":
        print("The difference of a-b is",a-b)
    elif c == "*":
        print("the multiplication of a*b is  ",a*b)
    elif c == "/":
        print("The division of a/b is ",a/b)
    else:
        print("Try again ")
play=input("Do you want to run again (y/n)".lower())
if not play=="y":
    running=False
print("Thank you for using our calculator")
