import re

my_str = "Hi my name is John and email address is john.doe@somecompany.co.uk and my friend's email is jane_d+oe124@gmail.com jane_d24@gm-ail.com "
emails = re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", my_str)

for mail in emails:
    print(mail)
