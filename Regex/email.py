from cgitb import text
import re


text = "my email is wangxq2022.go-like_geek@infosoft22.com, remember to email me."
# extract all email addresses and add them into the resulting set
new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text, re.I))

print(new_emails)
