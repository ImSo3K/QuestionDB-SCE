import examSystemData
import textData

print('initializing objects with the data from the given text files')
obj1 = examSystemData.Exam()
textData.get_exam_info(obj1)
textData.get_question_info(obj1)
obj2 = examSystemData.Course()
textData.get_course_info(obj2, obj1)
obj3 = examSystemData.Department()
textData.get_department_info(obj2, obj3)

print('Press 1 to print Department data')
print('Press 2 to print Course data')
print('Press 3 to print Exam data')
print('Press 4 to print Question data')
