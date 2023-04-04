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
# Define function to handle user input and output
def main():
    while True:
        name = input("Please enter your name (or 'q' to quit): ")
        if name == "q":
            break
        age = input("Please enter your age: ")
        while not age.isdigit():
            age = input("Invalid input. Please enter your age as a number: ")
        gender = input("Enter your gender ('Male'/ 'Female'): ")
        phone_number = input("Enter your phone number: ")
        while not phone_number.isdigit() and len(phone_number) != 10:
            phone_number = input("Invalid input. Please enter your phone number as a number: ")
        preferred_building = input("Enter your preferred building ('Dubai' or 'Novotel'): ")

        try:
            if preferred_building.lower() == 'dubai':
                result = assign_room(dubai_rooms, gender, name, age, phone_number)
            elif preferred_building.lower() == 'novotel':
                result = assign_room(novotel_rooms, gender, name, age, phone_number)
            else:
                raise ValueError(f"Invalid preferred building: {preferred_building}")
        except ValueError as e:
            print(str(e))
            continue

        print(result)

    print(dubai_rooms.items())
    print(novotel_rooms.items())
        
if __name__ == '__main__':
    main()
    
### File to have random list of participants to show that extreme cases work
## and also a show as example of the people entering their own details and being assigned
# Issue about  showing the available rooms to the user in case preferred building is unavailable
# Also issue about user input being wrong 
#Also handling 