Pi=3.14159

def cir():
    r=int(input("enter a radius for circumference "))
    c=2*Pi*r
    print(c)

def area():
    r=int(input("enter a radius "))
    a=Pi*r**2
    print(a)

def main():
    cir()
    area()

main()    