def Breakusingfor(number):
    for i in range(number+1):
        if i==6:
            break
        print(i)

def main():
    userinput=int(input("enter num plz: "))
    Breakusingfor(userinput)

main()    