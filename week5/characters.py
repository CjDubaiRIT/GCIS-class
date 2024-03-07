def character(name):
    print(name)
    c=0
    for i in range(len(name)):
        print(name[c])
        c=c+1

def reverse(name):
    print(name)
    c=-1
    for i in range(len(name)):
        print(name[c])
        c=c-1

def main():
    name=input("write a name")
    character(name)  
    reverse(name)      

main()    