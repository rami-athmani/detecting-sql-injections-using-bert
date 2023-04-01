import random

# Define sample data
first_names = ['Adam', 'Brianna', 'Cameron', 'Danielle', 'Ethan', 'Faith', 'Gavin', 'Haley', 'Isaac', 'Jasmine']
last_names = ['Anderson', 'Brown', 'Carter', 'Davis', 'Edwards', 'Fisher', 'Green', 'Harris', 'Irwin', 'Johnson']
genders = ['Male', 'Female']
ages = list(range(18, 101))
customer_ids = list(range(1, 1001))

# Define function to generate UPDATE statements
def generate_update_statement(customer_id, first_name, last_name, gender, age):
    return f"UPDATE customers SET first_name='{first_name}', last_name='{last_name}', gender='{gender}', age={age} WHERE customer_id={customer_id}"

# Generate 1000 UPDATE statements
for i in range(1000):
    customer_id = random.choice(customer_ids)
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    gender = random.choice(genders)
    age = random.choice(ages)
    update_statement = generate_update_statement(customer_id, first_name, last_name, gender, age)
    print(update_statement)