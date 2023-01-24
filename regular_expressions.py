import re

# pattern = re.compile('this')
pattern = re.compile(r"[a-zA-Z].[a]")
string = "search this inside of this text please."

a = pattern.search(string)
print(a.span)
print(a.group())
b = pattern.findall(string)
print(b)
c = pattern.fullmatch(string)  # needs exact full match of both strings
print(c)
d = re.compile("search").match(string)
print(d)

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
string = "d@d.de"
e = pattern.match(string)
print(e)

# password checker
pattern = re.compile(r"^[a-zA-Z0-9$%#@]{8,}\d")
password = 'supersecret123'
g = pattern.fullmatch(password)
print(g)

# better password checker
# requests a password with at least a small, a capital letter, a number and
# minimum 8 chars
pattern = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$")
password = 'supersecret123'
g = pattern.fullmatch(password)
print(g)
password = 'superseCret123'
g = pattern.fullmatch(password)
print(g)
