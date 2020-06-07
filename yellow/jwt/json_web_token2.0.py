import base64
import hmac
import hashlib

f = open("public.pem")
SECRET = f.read()
#RS => HS, login(test) => admin
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9Cg.eyJsb2dpbiI6ImFkbWluIn0K"

#python-2
#signature = base64.urlsafe_b64encode(hmac.new(SECRET, token, hashlib.sha256).digest()).decode("utf8").rstrip("=")

#python-3
signature = base64.urlsafe_b64encode(hmac.new(bytes(SECRET, encoding="utf8"), token.encode('utf-8'), hashlib.sha256).digest()).decode("utf8").rstrip("=")
print(token + "."+signature)
