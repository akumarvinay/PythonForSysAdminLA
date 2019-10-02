def display(message, count):
    try:
        for time in range(int(count)):
            print(f"{message}")
    except ValueError:
        print("Error: Invalid value entered")

message = input("Enter you message here: ")
count = input("Enter number of times you want to display message: ")
type(count)

display(message, count)

