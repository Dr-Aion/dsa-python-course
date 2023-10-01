class YouTube:
    def __init__(self, username, subscribers = 0, subscriptions = 0):
        self.username = username
        self.subscribers = subscribers
        self.subscriptions = subscriptions
    
    def subscribe(self, user):
        user.subscribers += 1
        self.subscriptions += 1

user1 = YouTube("Aiganym")
user2 = YouTube("Aizhan", 5)
user1.subscribe(user2)
print(user1.username)
print(user1.subscribers)
print(user1.subscriptions)


print(user2.username)
print(user2.subscribers)
print(user2.subscriptions)


