import glob
import os
import json
import shutil


try:
    os.mkdir("./processedfile")
except OSError:
    print("Folder ./processed already exists")

sourceFiles = glob.iglob("./new/receipt-[0-9]*")   # Using glob.iglob improve memory usage through iterator rather than loading all at once using glob.glob
finalVal = float(0.0)

#print(sourceFiles)

for path in glob.glob("./new/receipt-[0-9]*"):
    with open(path) as f:
        filecontent = json.load(f)
        finalVal += float(filecontent['value'])
    destpath = path.replace('new','processedfile')
    #destfile = path.split("/")[-1]
    #destpath = f"./processedfile/{destfile}"
    shutil.move(path,destpath)
    print(f"file {path} is moved to {destpath}")

#print("Final value after processing all files is $%.2f" % finalVal)
print(f"Final value after processing all files is ${round(finalVal, 2)}")

