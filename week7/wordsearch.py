def search(word):
    with open("C:\\Users\\ijjou\\OneDrive\\Desktop\\GCIS123\\GCIS-class\\GCIS-class\\week7\\wordsearchlist.txt") as myfile:
        while True:
            for i in myfile:
                length=len(i)
                stripped=i.strip()
            if stripped==word:
                print("Found the word:",word)
                break
            else:
                print("not found")
                break
                
def main():
    word=str(input("Enter a word to search in the file"))
    search(word)

main()