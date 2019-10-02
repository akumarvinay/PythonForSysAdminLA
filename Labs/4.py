filename = input("Enter the file name: ")
lineNumber = int(input("Enter the line number: "))
while True:
    if lineNumber == 0:
        lineNumber = int(input("Line Number cannot be zero, ReEnter the line number: "))
    else:
        break
#print(f"Line number entered is: {lineNumber}")
try:
    with open(filename, 'r') as file1:
        lines = file1.readlines()
        print(lines)
        count = int(len(lines))
        print(f"Count is {count} line number is {lineNumber}")
        if count >= lineNumber:
            print(f"requested line is: {lines[lineNumber-1].strip()}")
        else:
            print("specified (file is too short).")
except FileNotFoundError:
    print("Error: Please enter valid filename")
#except:
#    print("Error occured")


