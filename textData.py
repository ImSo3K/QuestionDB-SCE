import examSystemData

def get_department_list(obj):
    fo_dep = open('Departments.txt', 'r')
    line = fo_dep.readline().rstrip()
    obj.dep_name = line
    line = fo_dep.readline().rstrip()
    obj.coordinator_name = line
    fo_dep.close()


def get_courses_list(obj):
    fo_course = open('Courses.txt', 'r')
    line = fo_course.readline().rstrip()
    obj.course_name = line
    line = fo_course.readline().rstrip()
    obj.lecturer_name = line
    line = fo_course.readline().rstrip()
    obj.year_of_course = line
    fo_course.close()
    