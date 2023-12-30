import re
email = input("What's your email? ")

if re.search(".+@.+", email):
    print("Valid")
else:
    print("Invalid")
