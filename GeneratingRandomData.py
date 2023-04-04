import random
import string

# Define lists for the data you want to generate
names = ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Henry", "Isabel", "John","Issabella","Bernard","James","Syrus","Andy","Bobby","Cindy","Derek","Ethan","Fiona","Gavin","Hannah","Ivan","Jenny","Kenny","Linda","Mandy","Nancy","Oscar","Penny","Quincy","Randy","Sandy","Terry","Uma","Vicky","Wendy","Xavier","Yvonne","Zack"]
preferred_buildings = ["Dubai", "Novotel"]
genders = ["Male", "Female"]
ages = range(16, 26)

# Generate a list of phone numbers
phone_numbers = []
for i in range(10):
    phone_number = ''.join(random.choices(string.digits, k=10))
    phone_numbers.append(phone_number)

# Generate a list of dictionaries with the data
data = []
for i in range(650):
    name = random.choice(names)
    gender = random.choice(genders)
    preferred_building = random.choice(preferred_buildings)
    age = random.choice(ages)
    phone_number = random.choice(phone_numbers)
    print(f"{name} {gender} {preferred_building} {age} {phone_number}")
    data.append({"name": name, "gender": gender, "preferred_building": preferred_building, "age": age, "phone_number": phone_number})

# Print the data
# print(data)

for i in range (10):
    print(data[i])
