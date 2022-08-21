# Example of social media follow system
class User:
    def __init__(self, user_id, username):
        print("New user being created...")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        """Increases self follow count and user follower count"""
        user.followers += 1
        self.following += 1


user_1 = User("001", "mid-size sedan")
user_2 = User("002", "jack")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
