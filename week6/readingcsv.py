import csv

def readCSV(cFile):
    sum=0
    try:
        with open(cFile,'r') as csvFile:
            csv_reader=csv.reader(csvFile)
            next(csv_reader)
            for rowRecord in csv_reader:
                stripped=rowRecord.split()
                for i in rowRecord:
                    sum=sum+int(rowRecord)
                #print the sum of the first row on terminal
                print(sum)

    except FileNotFoundError:
        print("the file was not found")
    except IOError:
        print("theres another error")

def main():
    csvFile=input("enter file name with path: ")
    readCSV(csvFile)

if __name__=='__main__':
    main()


"""import csv

def calculate_class_average(csv_filename, column_number):
    total = 0
    count = 0

    with open(csv_filename, 'r') as file:
        csv_reader = csv.reader(file)
        
        # Skip the header
        next(csv_reader)
        
        for row in csv_reader:
            try:
                grade = float(row[column_number])
                total += grade
                count += 1
            except (IndexError, ValueError):
                # Skip rows with missing or invalid data
                continue

    if count > 0:
        class_average = total / count
        print(f"Class Average for column {column_number}: {class_average}")
    else:
        print("No valid grades found in the specified column.")

# Example usage:
calculate_class_average("grades.csv", 2)  # Assuming the grades are in the third column
"""