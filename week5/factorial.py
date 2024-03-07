def fact(r):
    sum=1
    for i in range(1,r):
        if i<=r:
            sum=sum*i
            print(sum)
            i=i+1


def main():
    r=int(input("enter a factorial number "))
    r=r+1
    fact(r)
    

main()    

