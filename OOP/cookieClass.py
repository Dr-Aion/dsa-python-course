class StarCookie:
    milk = 0.1
    def __init__(self, weight, color):
        self.weight = weight
        self.color = color

star_cookie1 = StarCookie(15, "Red")
# print(star_cookie1.weight)
# print(star_cookie1.color)

star_cookie2 = StarCookie(16, "Blue")
star_cookie2.milk = 0.2
StarCookie.milk = 0.3
print(star_cookie2.__dict__)
print(star_cookie1.__dict__)
print(StarCookie.__dict__)
