subjects = ["Maths", "Python", "DBMS", "AI"]

time_slots = ["9:00 AM", "11:00 AM", "2:00 PM"]

constraints = [
    ("Maths", "Python"),
    ("DBMS", "AI")
]

timetable = {}

def is_valid(subject, slot):
    for sub1, sub2 in constraints:
        if subject == sub1 and timetable.get(sub2) == slot:
            return False
        if subject == sub2 and timetable.get(sub1) == slot:
            return False

    return True

def backtracking(index):
    if index == len(subjects):
        return True

    subject = subjects[index]

    for slot in time_slots:
        if is_valid(subject, slot):
            timetable[subject] = slot

            if backtracking(index + 1):
                return True

            del timetable[subject]

    return False

if backtracking(0):
    print("Final Timetable:")
    for subject in subjects:
        print(subject, "->", timetable[subject])
else:
    print("No valid timetable found.")