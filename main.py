import random
import PySimpleGUI as sg
from tabulate import tabulate

timetable = {
    "Monday": {},
    "Tuesday": {},
    "Wednesday": {},
    "Thursday": {},
    "Friday": {},
    "Saturday": {},
}

# Enter the number of subjects
n = int(sg.popup_get_text("Enter the number of subjects: "))

# Enter the subjects
subjects = []
teaching_hours = {}
for i in range(n):
    subject = sg.popup_get_text(f"Enter subject {i+1}: ")
    subjects.append(subject)
    hours = int(sg.popup_get_text(f"Enter the number of teaching hours for {subject}: "))
    teaching_hours[subject] = hours

# Set time slots
start_time = 9
end_time = 16
time_slots = ["9.00", "10.00", "11.15", "12.15", "2.00", "3.00"]

# Assign subjects to time slots
for day, schedule in timetable.items():
    assigned_subjects = []
    for time_slot in time_slots:
        subject = random.choice(subjects)
        if subject in assigned_subjects:
            continue
        if time_slot not in schedule:
            schedule[time_slot] = subject
            assigned_subjects.append(subject)

# Create the table
table = []
for day, schedule in timetable.items():
    row = [day]
    for time_slot in time_slots:
        if time_slot in schedule:
            subject = schedule[time_slot]
            if subject in teaching_hours:
                row.append(subject)
            else:
                row.append(subject)
        else:
            row.append("")
    table.append(row)

# Create the GUI window
layout = [
    [sg.Table(values=table, headings=["Weeks"] + time_slots, justification="center", key="-TABLE-")],
    [sg.Button("Exit")]
]

window = sg.Window("Timetable", layout)

# Event loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Exit":
        break

window.close()