import re

# regex=r"(?=\w*)(?!.*[^a-zA-Z0-9])(?=^.{6,}$)"
# re1=r"(?=\w{4,})"

#no whitespace, cant start with digit, only alphanum_, 4+ length,
re1=r'(?=\w+@[a-zA-Z]{2,}\.[a-zA-Z]{2,})(?=^[a-zA-Z])'

str1='gg@mail.com'

print(re.match(re1,str1))