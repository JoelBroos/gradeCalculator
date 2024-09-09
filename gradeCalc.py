# Project: Student Grade Calculator
# Joel Broos 

import statistics
import tkinter

from tkinter import *
from tkinter import messagebox

totalExams = []  # list to contain exam results


# function to populate list with results
def mark_list():
    try:
        totalExams.append(float(examMk1.get()))
        newList = str(totalExams)
        # message box to display updated list for each entry
        messagebox.showinfo('Current list of exam results', newList)
        if len(totalExams) == 10:
            grade_calculator()
    except:
        print('Invalid or missing input')


# function to calculate results average
def grade_calculator():
    sumAllMrks = sum(totalExams)
    lowestMrk = min(totalExams)
    newTotal = sumAllMrks - lowestMrk
    divideNo = len(totalExams) - 1
    newAvg = newTotal/divideNo
    output = str(round(newAvg, 2))
    # message box to display average
    messagebox.showinfo('Exam Average', output)


# GUI initialising
window = Tk()
window.geometry("300x200")
window.title("Mark input")

# Adding GUI labels
markLabel = Label(window, text='Exam mark: ')
markLabel.grid(row='1', column='0')


# Adding exam mark entry box for user
examMk1 = StringVar()
ent1st = Entry(window, width=10, textvariable=examMk1)
ent1st.grid(row='1', column='1')


# button to add marks to list and compute avg when there are 10 results
btnAdd = Button(window, text='Next mark', width=10, command=mark_list)
btnAdd.grid(row='2', column='0', pady=5)


window.mainloop()