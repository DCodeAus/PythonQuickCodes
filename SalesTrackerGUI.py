#SalesTrackerGUI.py
# Similar to Assignment 2 Project 1: VideoTimes Logger Project with a GUI
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog


import os
class sales_tracker_GUI():
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("Sales Tracker GUI System")

        # Set the container frames
        self.top_frame = tk.Frame(self.main_window)
        self.result_frame = tk.Frame(self.main_window)
        self.bottom_frame = tk.Frame(self.main_window)

        # Get Sales  data.
        # Create and pack the widgets for Person's name .
        self.num_label = tk.Label(self.top_frame, text='Enter Number of Team Members :')
        self.num_entry = tk.Entry(self.top_frame, width=20)
        self.btn_write_sales_data = tk.Button(self.top_frame, text="Prepare Sales Report", command=self.write_sales_report)
        self.num_label.pack(side='left')
        self.num_entry.pack(side='left')
        self.btn_write_sales_data.pack(side='left')

        self.sales_report_text_area = tk.Text(self.result_frame, height=20, width=40)
        self.sales_report_text_area.configure(bg='light blue')
        self.btn_read_sales_data = tk.Button(self.bottom_frame, text="Display Sales Report", command=self.read_sales_report)
        self.btn_quit = tk.Button(self.bottom_frame, text="Quit", command=self.main_window.destroy)

        self.sales_report_text_area.pack()
        self.btn_read_sales_data.pack(side='left')
        self.btn_quit.pack(side='left')

        # Pack the frames.
        self.top_frame.pack()
        self.result_frame.pack()
        self.bottom_frame.pack()

        tk.mainloop()

    # GUI event handlers for write_sales_target() and read_sales_target() methods

    # write_sales_done() event handler
    def write_sales_report(self):

        # Get the number of staff in the sales team.
        try:
            num_staff = int(self.num_entry.get())

            # Open the file to hold the sales data.
            sales_file = open('sales_report.txt', 'w')
            # Get each staff's sales data and write it to the file.
            messagebox.showinfo("showinfo", "'Enter the sales data for each sales team member.'")
            for count in range(1, num_staff + 1):
                sales_data = float(simpledialog.askstring(title="Staff Staff # " + str(count) + "sales achieved)",
                                                        prompt="Enter Sales Data: "))

                sales_file.write(str(sales_data) + '\n')

            # Close the file.
            sales_file.close()
            messagebox.showinfo("showinfo", "The sales data info saved.\n Now click on Display Sales  Report button")
        except ValueError:
            messagebox.showinfo("Error", "Please enter a number")

    # read_sales_done() event handler
    def read_sales_report(self):
        disp_string = ""
        try:
            sales_file = open("sales_report.txt", 'r')
            # Initialise total variable to 0.0
            total = 0.0
            disp_string += "Here is the sales report for our team:"
            # Initialise a variable to keep count of the staff
            count = 0
            for line in sales_file:
                # convert a line to float
                sales_data = float(line)
                # Add 1 to the count variable
                count += 1
                # Display the sales data
                disp_string += "\nTeam Member #" + str(count) + ": " + str("${:,.2f}".format(sales_data))
                # Add the time to total
                total += sales_data

            disp_string += "\nTotal sales achieved: " + str("${:,.2f}".format(total))
            self.sales_report_text_area.insert('1.0', (disp_string))

            sales_file.close()
        except IOError:
            messagebox.showinfo("Error", "Could not open file")


myGUI = sales_tracker_GUI()
