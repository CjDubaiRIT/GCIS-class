"""example 1 is to return the largest number written 
by the user

def larger_number(num1,num2):
    if num1>num2:
        return num1
    else:
        return num2

def main():
    num1=int(input("enter a number "))
    num2=int(input("enter another number "))
    result=larger_number(num1,num2)
    print(result)

main()


"example 2 is about calculating an average number"

def calculateAv(n):
    sum=0
    for i in range(n):
        user=int(input("enter the number "))
        sum=sum+user
    return sum/n
    
def main():
    n=int(input("enter how many numbers would you like to have for the average"))
    print(calculateAv(n))

main()

def evennums():
    for i in range(1,21):
        if i % 2==0:
            print(i)

def main():
    evennums()

main()

def even():
    i=0
    
    while i<=20:
        
        if i%2==0:
            print(i)
        i=i+1

def main():
    even()
main()    


def repeat():
    i=1
    while i<=5:
        i=i+1
        print ("Hello World")

repeat()

def repeat():
    for i in range(1,6):
        print("Hello world")

repeat()

def repeat(c):
    n=0
    r=0
    while r <=c:
        n=n+c
        r=r+1
    print(n)    

def main():
    c=int(input("count"))
    repeat(c)

main()
"""