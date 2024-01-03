import re
#regular expresisons can be used to validate data, to cleanup data, to extract data
url = input("URL: ")

#1 replace() method of a string
# username = url.replace("https://twitter.com/", "")

#2 removeprefix() method of a string
# username = url.removeprefix("https://twitter.com/")

#3 re.sub(pattern, repl, string, count = 0, flags = 0)
# username = re.sub(r"^(https?://)?(www\.)twitter\.com/", "", url)

matches = re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE)
if matches:
    print(f" Username: ", matches.group(1))

#4 there's also re.split(pattern, string, maxsplit=0, flags=0)

#4 there's also re.findall(pattern, string, flags=0)