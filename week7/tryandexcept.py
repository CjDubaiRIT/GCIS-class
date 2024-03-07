def devision(a,b):
    sum=0
    while True:
        if a == "":
            break
        if b== "":
            break
        try:
            a=float(a)
            b=float(b)
            sum=a/b
            print(sum)
            break
        except ZeroDivisionError:
            print("denomiator is zero which is an error")
            break
        except ValueError:
            print("error")
            break

def main():
    a=input("Enter a numerator")
    b=input("enter a denominator")
    devision(a,b)

if __name__=="__main__":
    main()