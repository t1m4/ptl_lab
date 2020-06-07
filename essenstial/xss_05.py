#this script encode utf-8 in ascii code
uuid=list("alert('5477fae0-6fde-42c7-af14-feddcfd15e53')")
uuid_charcode=''
for i in uuid:
    if i != uuid[-1]:
        uuid_charcode+=str(ord(i))+','
    else:
        uuid_charcode+=str(ord(i))
print(uuid_charcode)
