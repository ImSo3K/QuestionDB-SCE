class Department:
    def __init__(self, dep_name='', coordinator_name=''):
        self.dep_name = dep_name
        self.coordinator_name = coordinator_name

    def __del__(self):
        print('Dep obj deleted')


class Course:
    def __init__(self, course_name='', lecturer_name='', year_of_course=''):
        self.course_name = course_name
        self.lecturer_name = lecturer_name
        self.year_of_course = year_of_course
        self.course_dep = Department()

    def __del__(self):
        print('Course obj deleted')


class Question:
    def __init__(self, **question_info):
        self.question_info = question_info

    def __del__(self):
        print('Question obj deleted')


class Exam:
    def __init__(self, exam_date):
        self.exam_date = exam_date
        self.exam_course = Course()
        self.question_list = [Question()]

    def __del__(self):
        print('Exam obj deleted')
