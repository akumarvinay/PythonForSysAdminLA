#!/usr/bin/env python3.6
from argparse import ArgumentParser
import requests

parser = ArgumentParser(description='Script got getting html response from Given URL')
parser.add_argument("url",help="Provide URl of website")
parser.add_argument("filename",help="Provide filename to store output")
parser.add_argument("--responseFormat",default="html",choices=['html','json'], help="Provide response format(Default is HTML)")
args = parser.parse_args()
url = args.url
responseFormat = args.responseFormat
content = None
print(f"Given URl is {url}\nResponse fromat is {responseFormat}")
#print(dir(response))
try:
    response = requests.get(url)
except ConnectionError as e:
    print(f"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXConnection error {e}")
    exit(1)
except:
    print("Error")
else:
    if response.status_code == 200:
        if args.responseFormat == "json":
            content = json.dump(response.json())
        else:
            content = response.text
        with open(args.filename, 'w+') as f:
            f.write(content)
        print(response.status_code)
    else:
        print(f"Error in respone code {response.status_code}")
##print(dir(response))
#print(f"Response code is {response.status_code}")
#print(f"Response content is {response.text}")


