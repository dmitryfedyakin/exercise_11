class Subject:
    '''
    Represents information about subject.
    '''
    
    def __init__(self, subj_name, classroom, time,
                 teach_name, teach_surname,
                 teach_patronymic, obj_type):
        '''
        Initializes information about subject.

        :param subj_name: Name of the subject
        :param classroom: Classroom where the subject is
        :param time: Time when subject is processing
        :param teach_name: Teacher name
        :param teach_surname: Teacher surname
        :param teach_patronymic: Teacher patronymic
        :param obj_type: Type of the subject
        '''
        
        self.subj_name = subj_name
        self.classroom = classroom
        self.time = time
        self.teach_name = teach_name
        self.teach_surname = teach_surname
        self.teach_patronymic = teach_patronymic
        self.obj_type = obj_type

    def __str__(self):
        '''
        Returns string representation of an object (for users).
        '''

        result = f'{self.time} {self.subj_name} {self.obj_type}'

        if self.teach_name != '' and \
        self.teach_surname != '' and \
        self.teach_patronymic != '':
            
            return f'{result}\n   Аудитория: {self.classroom}\n' \
                f'   Преподаватель - {self.teach_surname} ' \
                f'{self.teach_name} ' \
                f'{self.teach_patronymic}'
        
        return f'{result}\n   Аудитория: {self.classroom}'
 

class Schedule:
    '''
    Represents group schedule.

    Attributes:
        schedule_dict (dict): Dictionary consider information about table
    '''

    schedule_dict = {}

    def __init__(self, group):
        '''
        Initializes necessary group.

        :param group: Group we want to check
        '''
        
        self.group = group

    def add_subject(day, subject):
        '''
        Adds new subject to schedule

        :param day: Particular day with subjects
        :param subject: Subject that we want to add
        '''

        if day not in Schedule.schedule_dict:
            Schedule.schedule_dict[day] = []
        Schedule.schedule_dict[day].append(subject)

    def get_schedule(day):
        '''
        Get information about schedule on a particular day.

        :param day: Particular day

        :return: Schedule on particular day
        '''
        
        if day in Schedule.schedule_dict:
            return Schedule.schedule_dict[day]
        return []


class Load:
    '''
    Represents data load from file.
    '''
    
    def read_data(filename):
        '''
        Loads information about Table.

        :param filename: Name of the file
        '''

        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                data = line.strip().split(";")
                day = data[0]
                subject = Subject(data[1], data[2], data[3],
                                  data[4], data[5], data[6], data[7])
                Schedule.add_subject(day, subject)

     