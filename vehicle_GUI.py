#Vehicle_GUI.py
# Similar to Assignment 2 Project 3: Employee Management System Project with a GUI
# Used Vehicle_Inventory_Management_System_GUI
import vehicle
import pickle
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog


# Global constant for the filename
FILENAME = 'vehicles.dat'


# Initialising variable
dataLabel = ""


# Initialising the GUI
root = tk.Tk()
root.title("Vehicle Management System")
canvas = tk.Canvas(root)


def load_vehicles():
    try:
        # Open the vehicles.dat file.
        input_file = open(FILENAME, 'rb')

        # Unpickle the dictionary.
        vehicle_dct = pickle.load(input_file)

        # Close the idNumber_inventory.dat file.
        input_file.close()
    except IOError:
        # Could not open the file, so create
        # an empty dictionary.
        vehicle_dct = {}

    # Return the dictionary
    return vehicle_dct

# The save_vehicles funtion pickles the specified
# object and saves it to the vehicles file.
def save_vehicles(myvehicles):
    # Open the file for writing.
    output_file = open(FILENAME, 'wb')

    # Pickle the dictionary and save it.
    pickle.dump(myvehicles, output_file)

    # Close the file.
    output_file.close()


# The look_up function looks up an item in the
# specified dictionary.
def look_up():
    displayResult.delete('1.0', 'end')
    disp_string = ""
    myvehicles = load_vehicles()
    # Get an ID number to look up.
   #idNumber = int(input('Enter an ID number: '))
    idNumber = int(simpledialog.askstring(title="vehicle model ID Number)",
                         prompt="Please enter an vehicle model ID number: "))
    # Look it up in the dictionary.
    if idNumber in myvehicles:
        displayResult.insert('1.0', myvehicles.get(idNumber))
    else:
        messagebox.showinfo("Error", "That ID number couldn't be found.")

    # Save the y.
    #     return vehicle_dct myvehicle dictionary to a file.
    save_vehicles(myvehicles)


# The add function adds a new entry into the
# specified dictionary.
def add():
    displayResult.delete('1.0', 'end')
    myvehicles = load_vehicles()
    # Get the vehicle info.
    make = simpledialog.askstring(title="vehicle Make)",
                                            prompt="Please enter the Vehicle's make: ")
    idNumber = int(simpledialog.askstring(title="Vehicle ID Number)",
                                          prompt="Please enter an Vehicle ID number: "))
    mileage = simpledialog.askstring(title="Vehicle Mileage)",
                                            prompt="Please enter the Vehicle Mileage: ")
    price = simpledialog.askstring(title="Vehicle Price)",
                                            prompt="Please enter the Vehicle price: ")

    # Create an Vehicle object named entry.
    entry = vehicle.Automobile(make, idNumber, mileage, price)

    # If the name does not exist in the dictionary,
    # add it as a key with the entry object as the
    # associated value.
    if idNumber not in myvehicles:
        myvehicles[idNumber] = entry
        messagebox.showinfo("Successful", "The entry has been added.")
    else:
        messagebox.showinfo("Error", "That ID number already exists.")

    # Save the myvehicles dictionary to a file.
    save_vehicles(myvehicles)


# The change function changes an existing
# entry in the specified dictionary.
def change():
    displayResult.delete('1.0', 'end')
    myvehicles = load_vehicles()
    # Get an ID number to look up.
    idNumber = int(simpledialog.askstring(title="vehicle Model ID Number)",
                                          prompt="Please enter an vehicle model ID number: "))

    if idNumber in myvehicles:
        # Get a new make
        make = simpledialog.askstring(title="Vehicle make)",
                                      prompt="Please enter the new vehicle's make: ")

        # Select a new mileage.
        mileage = simpledialog.askstring(title="Vehicle's mileage)",
                                            prompt="Please enter the new Vehicle's mileage: ")

        # Select a new price.
        price = simpledialog.askstring(title="Vehicle Price)",
                                          prompt="Please enter the new Vehicle's price: ")

        # Create an vehicle object named entry.
        entry = vehicle.Automobile(make, idNumber, mileage, price)

        # Update the entry.
        myvehicles[idNumber] = entry
        messagebox.showinfo("Successful", "The information has been updated.")
    else:
        messagebox.showinfo("Error", "That ID number couldn't be found.")

    # Save the myvehicles dictionary to a file.
    save_vehicles(myvehicles)


# The delete function deletes an entry from the
# specified dictionary.
def delete():
    displayResult.delete('1.0', 'end')
    myvehicles = load_vehicles()
    # Get an ID number to look up.
    idNumber = int(simpledialog.askstring(title="vehicle ID Number)",
                                          prompt="Please enter an vehicleID number: "))

    # If the ID number is found, delete the entry.
    if idNumber in myvehicles:
        del myvehicles[idNumber]
        messagebox.showinfo("Successful", "Entry deleted")
    else:
        messagebox.showinfo("Error", "That ID number couldn't be found.")

    # Save the myvehicles dictionary to a file.
    save_vehicles(myvehicles)

def display():
    disp_string = ""
    displayResult.delete('1.0', 'end')
    myvehicles = load_vehicles()

    for model_id in myvehicles:
        disp_string += str(myvehicles[model_id])
        displayResult.insert('1.0', myvehicles.get(model_id))


# GUI Layout Initialisation
lblTitle = tk.Label(root, text = "Used Vehicle Inventory System")
lblTitle.configure(bg= 'grey', font=("Calibri", 20, "bold"))
btnLookUp = tk.Button(root, text="Look up  vehicle info", command=lambda: look_up())
btnLookUp.configure(font=("Calibri", 10, "bold"))
btnAdd = tk.Button(root, text="Add a new vehicle", command=lambda: add())
btnAdd.configure(font=("Calibri", 10, "bold"))
btnChange = tk.Button(root, text="Update vehicle Info", command=lambda: change())
btnChange.configure(font=("Calibri", 10, "bold"))
btnDelete = tk.Button(root, text="Delete a vehicle", command=lambda: delete())
btnDelete.configure(font=("Calibri", 10, "bold"))
btnDisplay = tk.Button(root, text="Display all vehicles", command=lambda: display())
btnDisplay.configure(font=("Calibri", 10, "bold"))
btnExit = tk.Button(root, text="Quit the program", command=root.destroy)
btnExit.configure(font=("Calibri", 10, "bold"))

displayResult = tk.Text(root, bg = 'light blue', height=30, width=40, wrap=tk.WORD)
displayResult.configure(font=("Calibri", 10, "bold"))

# GUI layout with grid layout manager
lblTitle.grid(row=0,columnspan = 3, column =0,padx=10, pady = 10)
btnLookUp.grid(row=1, column=0, padx=10, pady = 10)
btnAdd.grid(row=2, column=0, padx=10, pady = 10)
btnChange.grid(row=3, column=0, padx=10, pady = 10)
btnDelete.grid(row=4, column=0, padx=10, pady = 10)
btnDisplay.grid(row=5, column=0, padx=10, pady = 10)
btnExit.grid(row=6, column=0, padx=10, pady = 10)
displayResult.grid(row=1, rowspan=6, column=1, padx=10, pady = 10)

root.mainloop()
