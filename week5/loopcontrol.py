def loop():
    sum=0
    while True:
        a=int(input("Enter a number: "))
        if a==0:
            break
        if a % 2==0:
            continue  
        else:
            sum=sum+a
    print(sum)

loop()