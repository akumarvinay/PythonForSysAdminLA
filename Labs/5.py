import argparse

parser = argparse.ArgumentParser(description="Provide filename")
parser.add_argument('filename',help="Provide file name")
parser.add_argument('lineNumber',type=int, help="enter line number")
#print(dir(argparse.ArgumentParser))
args = parser.parse_args()
print(f"file : {args.filename} lineNumber is {args.lineNumber}")
try:
    lines = open(args.filename,'r+').readlines()
    if len(lines) > args.lineNumber:
        print(f"{lines[args.lineNumber-1]}")
    else:
        print("File is too short")
except FileNotFoundError:
    print("Error: File not found")
except IOError as i:
    print(f"Error is {i})")

