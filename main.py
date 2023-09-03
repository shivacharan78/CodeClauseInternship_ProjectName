#Random Password Generator
import string
import random
len=int(input("Enter Length of the Password:"))
lower=string.ascii_lowercase
upper=string.ascii_uppercase
digit=string.digits
symbols=string.punctuation
str=lower+upper+digit+symbols
x=random.sample(str,len)
password="".join(x)
print(password)