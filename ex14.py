s = '/usr/local/bin/python.exe'

s1 = s[1:].split("/",4)
s2 = ",".join(s1)
print(s2)
s3 = s.rsplit("/",1)
s4 = ",".join(s3)
print(s4)