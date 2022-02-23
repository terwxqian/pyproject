import re
 
regex = r"(\d+)\.(\d+)"

m = re.match(regex, "27.1835")
print(m.groups())

m = re.match(r"(\d+)\.?(\d+)?", "27")
print(m.groups())


# A Python program to demonstrate working of re.match().
# a sample function that uses regular expressionsto find month and day of a date.
def findMonthAndDate(string):
        
    regex = r"([a-zA-Z]+) (\d+)"
    match = re.match(regex, string)
        
    if match == None: 
        print ("Not a valid date")
        return
    
    print ("Given Data: %s" % (match.group()))
    print ("Month: %s" % (match.group(1)))
    print ("Day: %s" % (match.group(2)))
    
# Driver Code
findMonthAndDate("I was born on June 24")   
print("")  
findMonthAndDate("Jun 24")

'''
search ⇒ find something anywhere in the string and return a match object.
match ⇒ find something at the beginning of the string and return a match object.
>>> a = "123abc"
>>> re.match("[a-z]+",a)
None
>>> re.search("[a-z]+",a)
abc
'''