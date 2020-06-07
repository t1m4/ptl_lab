#---------------this script help you decrypt hash md5
import hashlib
str='admin'
hash=hashlib.md5(str.encode()) #encode - convert string into byte
print(hash.hexdigest()) # show in hex format
print(hash.digest()) #show in byte format
