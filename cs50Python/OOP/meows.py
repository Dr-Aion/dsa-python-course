# n: int  means  n should be an int
def meow(n: int) -> str:   
    return "meow \n" * n

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end = "")