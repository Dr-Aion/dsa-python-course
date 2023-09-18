a = 'spam'
b = list(a)
print(b)

c = 'spam spam spam'
print(c.split())

d = 'spam-spam1-spam2'
delimiter = '-'
e = d.split(delimiter)
print(e)
print(delimiter.join(e))

myList = [1, 2, 3, 4]
myList.sort()
print(myList)
print(sorted(myList))