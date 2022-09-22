# This program can only be run using python --version 2


# this is a simple mini cryptograpy script,
# that I use to encrypt some sensitive information,
# it will give me publick and private key, of which I will
# use to decrypt it whenever I want


def xor_crypt_string(data, key = 'my_secret_passwd', encode=False, decode=False):
  from itertools import izip, cycle
  import base64
  
  if decode:
    data = base64.decodestring(data)
  xored = ''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(data, cycle(key)))
  
  if encode:
    return base64.encodestring(xored).strip()
  return xored

secret = 'Software engineer, specializiing in mostly python, and other technologies like html/css, git, linux and others'
print('The ciper text is:')
print(xor_crypt_string(secret, encode=True))
print('The plain text is:')
print(xor_crypt_string(xor_crypt_string(secret, encode=True), decode=True))
