def add():
    file=open("C:\\Users\\ijjou\\OneDrive\\Desktop\\GCIS123\\GCIS-class\\GCIS-class\\week7\\read.txt")
    sum=0
    for line in file:
        stripped=line.strip()
        splitted=stripped.split()
        sum2=0
        for i in splitted:
            num=int(i)
            sum2=sum2+num
        sum=sum+sum2
    print(sum)

add()