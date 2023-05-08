#Vehicle_console.py
# Similar to Assignment 2 Project 3: Employee Management System Project with a Console
# Used Vehicle_Inventory_Management_System_Console
import vehicle
import pickle

# Global constants for menu choices

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5
DISPLAY = 6


# Global constant for filename
FILENAME = 'vehicles.dat'

# main function
def main():

    # Get vehicle dictionary.
    vehicles = load_vehicles()

    # Initialize variable for user choice.
    choice = 0

    # Process user requests until user quits.
    while choice != QUIT:

        choice = get_user_choice()

        if choice== LOOK_UP:
            look_up(vehicles)
        elif choice == ADD:
            add(vehicles)
        elif choice == CHANGE:
            change(vehicles)
        elif choice == DELETE:
            delete(vehicles)
        elif choice == DISPLAY:
            disp(vehicles)

    # Pickle the resulting dictionary.
    save_vehicles(vehicles)
    
def load_vehicles():
    try:
        # Open the file.
        input_file = open(FILENAME, 'rb')

        # Unpickle the dictionary.
        vehicle_dict = pickle.load(input_file)

        # Close the file.
        input_file.close()
    except IOError:
        # Could not open file.
        # Create empty dictionary.
        vehicle_dict = {}

    return vehicle_dict

def get_user_choice():

    # Display menu, get user choice, and validate it.
    print()
    print('Menu')
    print('----------------------------------------')
    print('1. Look up a vehicle info')
    print('2. Add a new vehicle info')
    print('3. Change an existing vehicle info')
    print('4. Delete a vehicle info')
    print('5. Quit the program')
    print('6. Display all vehicles')
    print()

    choice = int(input('Enter your choice: '))

    # Validate the choice.
    while choice < LOOK_UP or choice > DISPLAY:
        choice = int(input('The choice you entered is invalid.'
                           ' Please enter a valid choice: '))

    # Return user's choice.
    return choice

def look_up(vehicles):
    # Get an vehicle model ID to look up.
    model_id = input('Enter an vehicle model ID number: ')

    # Look ID up in the dictionary. If found,
    # data will print using vehicle __str__ method
    # otherwise will print specified message.
    print(vehicles.get(model_id, "The specified ID number was not found"))

def add(vehicles):
    # Add vehicle  information.
    make = input('Enter vehicle make: ')
    model_id = input('Enter vehicle model ID number: ')
    mileage = input('Enter vehicle mileage: ')
    price = input('Enter vehicle price: ')

    new_auto = vehicle.Automobile(make, model_id, mileage, price)

    # Add new vehicle if ID does not exist.
    # otherwise notify user that ID exists.
    if model_id not in vehicles:
        vehicles[model_id] = new_auto
        print('The new vehicle info has been added.')
    else:
        print('A vehicle with that ID already exists.')

def change(vehicles):
    # Update vehicle information.
    model_id = input('Enter vehicle model ID number: ')

    # Change vehicle information if ID exists.
    # Otherwise, notify user that ID does not exist.
    if model_id in vehicles:
        make = input('Enter the new make: ')
        mileage = input('Enter the new mileage: ')
        price = input('Enter the new price: ')

        new_auto = vehicle.Automobile(make, model_id, mileage, price)

        vehicles[model_id] = new_auto
        print('Vehicle information updated.')
    # vehicle model ID not found.
    else: 
        print('The specified ID number was not found.')


def delete(vehicles):
    # Delete vehicle  information.
    model_id = input('Enter vehicles model ID: ')

    # Change vehicle information if model_id exists.
    # Otherwise, notify user that ID does not exist.
    if model_id in vehicles:
        del vehicles[model_id]
        print('Vehicle information deleted.')
    # ID not found.
    else: 
        print('The specified ID number was not found.')

def disp(vehicles):
    dictionary_items = vehicles.items()
    for model_id in vehicles:
        print("=================")
        print(str(vehicles[model_id]))


# Function pickles the specified dictionary and
# saves it to the vehicles file.
def save_vehicles(vehicles):
    # Open the file for writing.
    output_file = open(FILENAME, 'wb')

    # Pickle the dictionary and save it.
    pickle.dump(vehicles, output_file)

    # Close the file.
    output_file.close()


main()