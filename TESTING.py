num_rooms = 25 
dubai_rooms = {"Floor1": {f'Room {i+1}':[] for i in range(num_rooms)} , "Floor2":{f'Room {i+1}':[] for i in range(num_rooms)},"Floor3":{f'Room {i+1}':[] for i in range(num_rooms)}}
novotel_rooms ={"Floor1": {f'Room {i+1}':[] for i in range(num_rooms)} , "Floor2":{f'Room {i+1}':[] for i in range(num_rooms)},"Floor3":{f'Room {i+1}':[] for i in range(num_rooms)}}

def assign_room(preferred_building, gender, name, age, phone_number):
    if gender.lower() == 'female':
        # Assign to a room in Second floor of preferred building
        for floor, rooms in preferred_building.items():
            if floor == 'Floor2':
                for room, occupants in rooms.items():
                    if len(occupants) < 4 and sum(1 for occupant in occupants if occupant['gender'].lower() == 'female') < 4:
                        occupants.append({'name': name, 'gender': gender.lower(), 'age': age, 'phone_number': phone_number})
                        if preferred_building == dubai_rooms:
                            preferred_building = "Dubai"
                        else:
                            preferred_building = "Novotel"
                        return f"{name}  has been assigned to {floor}, {room} in the {str(preferred_building)} building."

        # If all rooms are full on second floor, assign to a room in third floor
        for floor, rooms in preferred_building.items():
            if floor == 'Floor3':
                for room, occupants in rooms.items():
                    if len(occupants) < 4 and sum(1 for occupant in occupants if occupant['gender'].lower() == 'female') < 4:
                        occupants.append({'name': name, 'gender': gender.lower(), 'age': age, 'phone_number': phone_number})
                        if preferred_building == dubai_rooms:
                            preferred_building = "Dubai"
                        else:
                            preferred_building = "Novotel"
                        return f"{name}  has been assigned to {floor}, {room} in the {str(preferred_building)} building."
        # If all rooms in preferred building are full, try assigning to the other building
        if preferred_building == dubai_rooms:
            other_building = novotel_rooms
            building_name = "Novotel"
        else:
            other_building = dubai_rooms
            building_name = "Dubai"

        for floor, rooms in other_building.items():
            for room, occupants in rooms.items():
                if len(occupants) < 4 and sum(1 for occupant in occupants if occupant['gender'].lower() == 'female') < 4:
                    occupants.append({'name': name, 'gender': gender.lower(), 'age': age, 'phone_number': phone_number})
                    return f"{name}  has been assigned to {floor}, {room} in the {building_name} building."
       
        # If all rooms are full, return error message
        return f"Sorry {name} , both buildings are full. You will have to find a hostel."

    elif gender.lower() == 'male':
        # Assign to a room in first floor of preferred building
        for floor, rooms in preferred_building.items():
            if floor == 'Floor1':
                for room, occupants in rooms.items():
                    if len(occupants) < 4 and sum(1 for occupant in occupants if occupant['gender'].lower() == 'male') < 4:
                        occupants.append({'name': name, 'gender': gender.lower(), 'age': age, 'phone_number': phone_number})
                        if preferred_building == dubai_rooms:
                            preferred_building = "Dubai"
                        else:
                            preferred_building = "Novotel"
                        return f"{name}  has been assigned to {floor}, {room} in the {str(preferred_building)} building."

        # If all rooms are full on first floor, assign to a room in third floor
        for floor, rooms in preferred_building.items():
            if floor == 'Floor3':
                for room, occupants in rooms.items():
                    if len(occupants) < 4 and sum(1 for occupant in occupants if occupant['gender'].lower() == 'male') < 4:
                        occupants.append({'name': name, 'gender': gender.lower(), 'age': age, 'phone_number': phone_number})
                        if preferred_building == dubai_rooms:
                            preferred_building = "Dubai"
                        else:
                            preferred_building = "Novotel"
                        return f"{name}  has been assigned to {floor}, {room} in the {str(preferred_building)} building."
        # If all rooms in preferred building are full, try assigning to the other building
        if preferred_building == dubai_rooms:
            other_building = novotel_rooms
            building_name = "Novotel"
        else:
            other_building = dubai_rooms
            building_name = "Dubai"

        for floor, rooms in other_building.items():
            for room, occupants in rooms.items():
                if len(occupants) < 4 and sum(1 for occupant in occupants if occupant['gender'].lower() == 'male') < 4:
                    occupants.append({'name': name, 'gender': gender.lower(), 'age': age, 'phone_number': phone_number})
                    return f"{name}  has been assigned to {floor}, {room} in the {building_name} building."
        # If all rooms are full, return error message
        return f"Sorry {name} , both buildings are full. You will have to find a hostel."

    # If gender is not male or female, return error message
    return f"Sorry {name}, we cannot assign a room to someone of gender '{gender}'."
# # Open input file for reading
# with open('Data.txt', 'r') as input_file:
#     # Read input from file
#     input_data = input_file.readlines()
    
# # Process input
# with open('ResultOfTest', 'w') as output_file:
#     for line in input_data:
#         name, gender,preferred_building,age,phone_number = line.strip().split()
#         try:
#             if preferred_building.lower() == 'dubai':
#                 output_file.write = assign_room(dubai_rooms, gender, name, age, phone_number)
#             elif preferred_building.lower() == 'novotel':
#                 output_file.write = assign_room(novotel_rooms, gender, name, age, phone_number)
#             else:
#                 raise ValueError(f"Invalid preferred building: {preferred_building}")
#         except ValueError as e:
#             print(str(e))

def read_input_file(file_name):
    input_data = []
    with open(file_name, 'r') as file:
        for line in file:
            input_data.append(tuple(line.strip().split()))
    return input_data


def write_output_file(file_name, output_data):
    with open(file_name, 'w') as file:
        for line in output_data:
            file.write(line +'\n' )


def process_input_data(input_data):
    output_data = []
    for data in input_data:
        name, gender , preferred_building,age,phone_number = data
        if preferred_building.lower() == 'dubai':
            result = assign_room(dubai_rooms, gender, name, age, phone_number)
        elif preferred_building.lower() == 'novotel':
            result = assign_room(novotel_rooms, gender, name, age, phone_number)
        else:
            result = f"Invalid preferred building '{preferred_building}'."
            output_data.append(result)
        output_data.append(result)
    return output_data


input_file_name = 'Data.txt'
output_file_name = 'ResultOfTest.txt'
input_data = read_input_file(input_file_name)
output_data = process_input_data(input_data)
write_output_file(output_file_name, output_data)