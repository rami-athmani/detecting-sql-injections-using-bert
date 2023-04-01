import random

# Define sample data
first_names = ['John', 'Jane', 'Alice', 'Bob', 'Eva', 'James', 'Olivia', 'David', 'Sophia', 'William']
last_names = ['Doe', 'Smith', 'Johnson', 'Williams', 'Lee', 'Taylor', 'Brown', 'Wilson', 'Clark', 'Jackson']
genders = ['Male', 'Female']
ages = list(range(18, 101))
customer_ids = list(range(1, 1001))

# Define function to generate INSERT statements
def generate_insert_statement(customer_id, first_name, last_name, gender, age):
    return f"INSERT INTO customers (customer_id, first_name, last_name, gender, age) VALUES ({customer_id}, '{first_name}', '{last_name}', '{gender}', {age})"

# Generate 1000 INSERT statements
for i in range(1000):
    customer_id = random.choice(customer_ids)
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    gender = random.choice(genders)
    age = random.choice(ages)
    insert_statement = generate_insert_statement(customer_id, first_name, last_name, gender, age)
    print(insert_statement)