def readFile():
    my_file = open("GCIS-class/week6/hello.txt",'r')
    sum=0
    for line in my_file:
        strippedstring=line.strip()
        splittedstring=strippedstring.split()
        for i in splittedstring:
            sum=sum+int(line)
    print(sum)
    my_file.close()

def main():
    readFile()

if __name__=='__main__':
    main()