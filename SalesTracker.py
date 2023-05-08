#SalesTracker Program
#Problem is to prepare a sales report for the company team
# Code the input and creation of the file "sales_report.txt"
# Similar to Assignment 2 Project 1: VideoTimes Logger Project

# This program saves a sequence of sales data report
# to the sales_report.txt file.

def save_sales_report():
    # Get the number of staff in the sales team.
    num_staff = int(input('How many staff are in the sales team? '))

    # Open the file to hold the sales data.
    sales_file = open('sales_report.txt', 'w')

    # Get each staff's sales data and write
    # it to the file.
    print('Enter the sales data for each staff.')
    for count in range(1, num_staff + 1):
        sales_data = float(input(f'Sales Staff #{count}: '))
        sales_file.write(f'{sales_data}\n')

    # Close the file.
    sales_file.close()
    print('The data have been saved to sales_report.txt.')



# Code the display of the data

def read_sales_report():
    # This program reads the values in the sales_report.txt
    # file and calculates their total.

    # Open the sales_report.txt file for reading.
    sales_file = open('sales_report.txt', 'r')

    # Initialize an accumulator to 0.0.
    total = 0.0

    # Initialize a variable to keep count of the staff.
    count = 0

    print('Here is the sales data report from each staff:')

    # Get the values from the file and total them.
    for line in sales_file:
        # Convert a line to a float.
        sales_data = float(line)

        # Add 1 to the count variable.
        count += 1

        # Display the time.
        print(f'Sales Staff No. #{count}: {sales_data}')

        # Add the time to total.
        total += sales_data

    # Close the file.
    sales_file.close()

    # Display the total of the running times.
    print(f'A total of {"${:,.2f}". format(total)} sales achieved.')


save_sales_report()
read_sales_report()

