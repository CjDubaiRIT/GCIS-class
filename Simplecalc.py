#try subtraction,multiply and modulus
"""
def add(a,b):
    x=a+b
    print(x)

def sub(a,b):
    x=a-b
    print(x)

def mult(a,b):
    x=a*b
    print(x)
def main():
    a=int(input("Please enter a number: "))
    b=int(input("Please enter another number: "))
    add(a,b)
    sub(a,b)
    mult(a,b)

main()


#int(input("")) to let the computer know that the user input is a number not a string(letters)
ask=input("Would you like to add, subtract or multiply? ")
if ask=='add':
    a=int(input("Please enter a number: "))
    b=int(input("Please enter another number: "))
    add(a,b)
elif ask=='subtract':
    a=int(input("Please enter a number: "))
    b=int(input("Please enter another number: "))
    sub(a,b)
elif ask=='multiply':
    a=int(input("Please enter a number: "))
    b=int(input("Please enter another number: "))
    mult(a,b)
    

def add(a,b):
    x=a+b
    #print(x)
    return x

def sub(a,b):
    x=a-b
    #print(x)
    return x
def mult(a,b):
    x=a*b
    #print(x)
    return x

a=int(input("Please enter a number: "))
b=int(input("Please enter another number: "))
x=add(a,b)
print(x)
x=sub(a,b)
print(x)
x=mult(a,b)
print(x)

def add(a,b):
    x=a+b
    #print(x)
    return x

def sub(a,b):
    x=a-b
    #print(x)
    return x
def mult(a,b):
    x=a*b
    #print(x)
    return x
def main():
    a=int(input("Please enter a number: "))
    b=int(input("Please enter another number: "))
    x=add(a,b)
    print(x)
    y=sub(x,b)
    print(y)
main()
"""