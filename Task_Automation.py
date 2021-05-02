# task Automation Project

from tkinter import *
from datetime import datetime
from csv import writer

# setting up of the GUI (Main window)

window = Tk()
window.geometry("460x450")
window.title("Time Tracking System")

# setting up labels used in GUI

Label(window, text="Welcome to Task Automation", font=("arial", 16, "bold")).pack()

Label(window, text="Enter Project Name:", font=("arial", 12)).place(x=10, y=70)
Label(window, text="e.g. File Processing", font=("arial", 10)).place(x=230, y=95)

Label(window, text="Enter Start Date and Time:", font=("arial", 12)).place(x=10, y=150)
Label(window, text="dd/mm/yy      hh:mm (24hr format)", font=("arial", 10)).place(x=230, y=170)

Label(window, text="Enter End Date and Time:", font=("arial", 12)).place(x=10, y=230)
Label(window, text="dd/mm/yy      hh:mm (24hr format)", font=("arial", 10)).place(x=230, y=250)

# variables to hold default text in text boxes

pn = StringVar()
fn = StringVar()
sn = StringVar()

# setting up text boxes used in GUI

entry_1 = Entry(window,textvar=pn, width=20, font=('Helvetica', 12))
entry_1.place(x=230, y=70)
entry_1.insert(0, 'Task 1')

entry_2 = Entry(window,textvar=fn, width=20, font=('Helvetica', 12))
entry_2.place(x=230, y=150)
entry_2.insert(0, '27/07/21     11:00')

entry_3 = Entry(window,textvar=sn, width=20, font=('Helvetica', 12))
entry_3.place(x=230, y=230)
entry_3.insert(0, '27/07/21     13:30')

# Initialization of constants

HOURS_IN_A_DAY = 24
SECONDS_IN_AN_HOUR = 3600
AMT_PER_HOUR = 5

# initializing an empty list
new_list = []

# function to get the number of hours and calculate revenue


def calc():
    global new_list                                                 # referencing the list created outside the function
    project_name = entry_1.get()                                    # getting text in the text boxes
    start_date = entry_2.get()
    end_date = entry_3.get()

    date_time_obj1 = datetime.strptime(start_date, '%d/%m/%y %H:%M')  # converting user string data into date
    date_time_obj2 = datetime.strptime(end_date, '%d/%m/%y %H:%M')
    diff = date_time_obj2 - date_time_obj1                            # calculating difference between dates
    number_of_days = diff.days                                        # getting number of days from difference
    days_to_hours = number_of_days * HOURS_IN_A_DAY                   # calculating hours from the days
    number_of_hours = diff.seconds/SECONDS_IN_AN_HOUR                 # calculating hours from the seconds
    total_hours = days_to_hours + number_of_hours                     # calculating total hours
    revenue = total_hours * AMT_PER_HOUR                              # calculating revenue due
    output_string = 'revenue  is  $ ' + str(revenue)
    Label(window, text=output_string, width=20, font=("arial", 12)).place(x=140, y=370)
    new_list = [project_name, start_date, end_date, total_hours, revenue]  # modifying the global list
    save(new_list)                                                         # calling the save function


# function to save user input data and calculated revenue into a csv file

def save(a_list):
    with open('TaskAutomation.csv', 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(a_list)

# initializing a button to call the calc function when clicked

button1 = Button(window, text="Calculate Revenue", fg='white', bg='brown', command=calc, relief=RIDGE, font=("arial", 12, "bold"))
button1.place(x=160, y=310)

window.mainloop()
