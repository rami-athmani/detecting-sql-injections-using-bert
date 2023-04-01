import random

# list of sample data for WHERE clause
ages = [18, 21, 25, 30, 35, 40, 45, 50, 55, 60]
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose']
states = ['NY', 'CA', 'IL', 'TX', 'AZ', 'PA', 'TX', 'CA', 'TX', 'CA']

# list of sample columns for SELECT clause
columns = ['id', 'first_name', 'last_name', 'age', 'city', 'state', 'salary']

# generate 2000 random SELECT statements
for i in range(2000):
    # generate random pattern
    pattern = random.randint(1, 3)
    
    if pattern == 1:
        # SELECT specific columns without WHERE clause
        num_columns = random.randint(1, len(columns))
        select_columns = random.sample(columns, num_columns)
        query = f"SELECT {', '.join(select_columns)} FROM employees"
    elif pattern == 2:
        # SELECT specific columns with WHERE clause
        num_columns = random.randint(1, len(columns) - 3)
        select_columns = random.sample(columns, num_columns)
        while 'age' in select_columns or 'city' in select_columns or 'state' in select_columns:
            select_columns = random.sample(columns, num_columns)
        age = random.choice(ages)
        city = random.choice(cities)
        state = random.choice(states)
        query = f"SELECT {', '.join(select_columns)} FROM employees WHERE age = {age} AND city = '{city}' AND state = '{state}'"
    else:
        # SELECT with aggregate function and GROUP BY clause
        column = random.choice(columns)
        num_columns = random.randint(1, len(columns) - 1)
        select_columns = random.sample(columns, num_columns)
        while column in select_columns:
            select_columns = random.sample(columns, num_columns)
        age_range = random.choice([(18, 25), (26, 35), (36, 45), (46, 60)])
        query = f"SELECT {', '.join(select_columns)}, AVG(salary) FROM employees WHERE age >= {age_range[0]} AND age <= {age_range[1]} GROUP BY {column}"
        
    print(query)
