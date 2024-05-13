from solution_4 import Load, Schedule

schedule = Load.read_data('raspisanie.txt')
for day in Schedule.schedule_dict:
    subjects = Schedule.get_schedule(day)
    print(f'\n{day}\n')
    for subject in subjects:
        print(subject)