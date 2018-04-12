import hashlib

m = hashlib.md5()
m.update(b"Hello")
print(m.hexdigest()) #16进制格式hash

s = hashlib.sha1()
s.update(b"Hello")
print(s.hexdigest())

s1 = hashlib.sha256
s1.update("Hello")
print(s1.hexdigest())