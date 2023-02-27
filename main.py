from user import User

app_user_one = User("hello@.com", "sarah smith", "pwd", "DevOps Engineer")
app_user_one.get_user_info()

app_user_two = User("newuser@.com", "james bond", "secret", "Agent")
app_user_two.get_user_info()