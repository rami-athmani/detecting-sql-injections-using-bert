import random

# Define sample data
usernames = ['user1', 'user2', 'user3', 'user4', 'user5', 'user6', 'user7', 'user8', 'user9', 'user10']
passwords = ['password1', 'password2', 'password3', 'password4', 'password5', 'password6', 'password7', 'password8', 'password9', 'password10']
emails = ['user1@example.com', 'user2@example.com', 'user3@example.com', 'user4@example.com', 'user5@example.com', 'user6@example.com', 'user7@example.com', 'user8@example.com', 'user9@example.com', 'user10@example.com']
ages = list(range(18, 101))
user_ids = list(range(1, 1001))
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose']
states = ['New York', 'California', 'Illinois', 'Texas', 'Arizona', 'Pennsylvania', 'Florida', 'Ohio', 'Michigan', 'Georgia']
zip_codes = [str(random.randint(10000, 99999)) for i in range(100)]

# Define function to generate DELETE statements
def generate_delete_statement(user_id, username, password, age, city, state):
    return f"DELETE FROM users_table WHERE user_id = {user_id} AND username = '{username}' AND password = '{password}' AND age = {age} AND city = '{city}' AND state = '{state}'"

# Generate 1000 DELETE statements
for i in range(1000):
    user_id = random.choice(user_ids)
    username = random.choice(usernames)
    password = random.choice(passwords)
    age = random.choice(ages)
    city = random.choice(cities)
    state = random.choice(states)
    delete_statement = generate_delete_statement(user_id, username, password, age, city, state)
    print(delete_statement)
