content = ""
filename = input("Please enter the File name: ")
print("Please enter conetent for file. End of input is empty line")
with open(filename, "w+") as f:
    while True:
        lines = input()
        if not lines.strip():
            print("End of Input")
            break
        else:
            content += lines+"\n"
    if not content.strip():
        print("Nothing to write in File")
    else:
        f.write(content)

print(f"line entered in files are :\n{content}")

