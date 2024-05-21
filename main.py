import random
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
n = int(input("Enter the number of subjects: "))

# Enter the subjects
subjects = []
for i in range(n):
    subject = input(f"Enter subject {i+1}: ")
    subjects.append(subject)

# Enter the number of teaching hours for each subject
teaching_hours = {}
for subject in subjects:
    hours = int(input(f"Enter the number of teaching hours for {subject}: "))
    teaching_hours[subject] = hours

# Set time slots
start_time = 9
end_time = 16
time_slots = [f"{time}:00" for time in range(start_time, 11)] + ["11:00", "11:15"] + [f"{time}:00" for time in range(11, 13)] + ["13:15", "14:00"] + [f"{time}:00" for time in range(15, end_time)]

# Assign subjects to time slots
for day, schedule in timetable.items():
    assigned_subjects = []
    for time_slot in time_slots:
        subject = random.choice(subjects)
        if subject in assigned_subjects:
            continue
        if time_slot not in schedule and time_slot != "11:00" and time_slot != "11:15":
            schedule[time_slot] = subject
            assigned_subjects.append(subject)
        else:
            while time_slot in schedule or subject in assigned_subjects or time_slot == "11:00" or time_slot == "11:15":
                time_slot = random.choice(time_slots)
                subject = random.choice(subjects)
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

# Print the timetable table
headers = ["Weeks"] + time_slots
tabulate(table, headers=headers, tablefmt="grid")
print(tabulate(table, headers=headers, tablefmt="grid"))