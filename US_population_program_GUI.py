#US_population_Program_GUI.py
# Similar to Assignment 2 Project 2: Fitness Tracker Project with a GUI
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog


import os
class US_pop_stats_GUI():
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("US Population Stats Display System")

        # Set the container frames
        self.top_frame = tk.Frame(self.main_window)
        self.button_frame = tk.Frame(self.main_window)
        self.avg_change_frame = tk.Frame(self.main_window)
        self.grt_inc_frame = tk.Frame(self.main_window)
        self.sml_inc_frame = tk.Frame(self.main_window)

        # Get person data.
        # Create and pack the widgets for Person's name .
        self.name_label = tk.Label(self.top_frame, text='Population Stats Program')
        self.name_label.pack()

        # Create a display button and a Quit button.
        self.display_button = tk.Button(self.button_frame, text='Display', command=self.display_pop_stats)
        self.quit_button = tk.Button(self.button_frame, text='Quit', command=self.main_window.destroy)
        # Pack the Buttons.
        self.display_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Create info display multiline text area
        self.avg_change_label = tk.Label(self.avg_change_frame, text='The average annual change:  ')
        self.avg_change_text_area = tk.Text(self.avg_change_frame,bg ='light blue', height = 2,width = 10)
        self.avg_change_label.pack(side = 'left',padx=5,pady =10)
        self.avg_change_text_area.pack(side = 'left',padx=5,pady =10)

        # Create info display multiline text area
        self.grt_inc_label = tk.Label(self.grt_inc_frame, text='The year with greatest increase:')
        self.grt_inc_text_area = tk.Text(self.grt_inc_frame, bg='light blue', height=2, width=10)
        self.grt_inc_label.pack(side = 'left',padx=5,pady =10)
        self.grt_inc_text_area.pack(side = 'left',padx=5,pady =10)

        # Create info display multiline text area
        self.sml_inc_label = tk.Label(self.sml_inc_frame, text='The year with  smallest increase:')
        self.sml_inc_text_area = tk.Text(self.sml_inc_frame, bg='light blue', height=2, width=10)
        self.sml_inc_label.pack(side = 'left',padx=5,pady =10)
        self.sml_inc_text_area.pack(side = 'left',padx=5,pady =10)

        # Pack the frames.
        self.top_frame.pack()
        self.button_frame.pack()
        self.avg_change_frame.pack()
        self.grt_inc_frame.pack()
        self.sml_inc_frame.pack()
        # Wait in the main loop until event handler click
        tk.mainloop()


    # event handler call back function (display person info button
    def display_pop_stats(self):
        disp_string = []
        input_file = open("USPopulation.txt", 'r')
        # Initialise total variable to 0.0
        total = 0.0
        # Setup variables
        yearly_change = []
        change = 0.0
        total_change = 0.0
        average_change = 0.0
        greatest_increase = 0.0
        smallest_increase = 0.0
        greatest_year = 0
        smallest_year = 0

        # Constant for the base year
        BASE_YEAR = 1950

        try:
            # Read all the lines in the file into a list.
            yearly_population = input_file.readlines()

            # Turn all read strings into numbers.
            for i in range(len(yearly_population)):
                yearly_population[i] = float(yearly_population[i])
            # Calculate the change in population size for each two years.
            for i in range(1, len(yearly_population)):
                change = yearly_population[i] - yearly_population[i - 1]
                yearly_change.append(change)
                # If this is the first year, set trackers to its value.
                if i == 1:
                    greatest_increase = change
                    smallest_increase = change
                    greatest_year = 1
                    smallest_year = 1
                    # This is not the first change in population size.
                    # Update trackers if relevant.
                else:
                    if change > greatest_increase:
                        greatest_increase = change
                        greatest_year = i
                    elif change < smallest_increase:
                        smallest_increase = change
                        smallest_year = i

            total_change = float(sum(yearly_change))
            average_change = total_change / len(yearly_change)
            average_change = format(average_change, ',.2f')

            self.avg_change_text_area.insert('1.0', average_change)
            self.grt_inc_text_area.insert('1.0', BASE_YEAR + greatest_year)
            self.sml_inc_text_area.insert('1.0', BASE_YEAR + smallest_year)

            input_file.close()

        except IOError:
            messagebox.showinfo('IOError','The file could not be found.')
        except IndexError:
            messagebox.showinfo('IndexError', 'There was an indexing error.')
        except:
            messagebox.showinfo('Error', 'An error occured')


pop_gui = US_pop_stats_GUI()

