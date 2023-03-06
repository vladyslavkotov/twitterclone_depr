import re

re1=r'^\w+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$'
str1='gh@mail.co'

print(re.match(re1,str1))