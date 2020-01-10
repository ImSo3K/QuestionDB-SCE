import examSystemData
import textData
import pdf2png
import png2docx
import Actions


def init_and_menu():
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
    print('Press 4 to convert pdf2image & then image2docx')
    print('Press 5 to log in')
    print('Press 0 to exit')
    while True:
        choice = input()

        if choice == '1':
            print(f'Department Name : {obj3.dep_name}\n' + f'Department Coordinator Name : {obj3.coordinator_name}')

        elif choice == '2':
            print(f'Course Name : {obj2.course_name}\n' + f'Course Lecturer Name : {obj2.lecturer_name}')
            print(f'Year Of Course : {obj2.year_of_course}')

        elif choice == '3':
            print(f'Exam Date : {obj2.exam.exam_date}\n' + f'Exam semester : {obj2.exam.exam_semester}')
            print('Question list :\n')
            for i in obj2.exam.question_list:
                examSystemData.Question.print_question_info(i)

        elif choice == '4':
            pdf2png.pdf_2_image()
            png2docx.image_2_docx()

        elif choice == '5':
            while True:
                print('1 - to log in as Coordinator')
                print('2 - to log in as Lecturer')
                print('3 - to log in as Student')
                print('0 - to exit log-in menu')
                log_choice = input()
                if log_choice == '1':
                    Actions.interface('Coordinator', obj1)

                elif log_choice == '2':
                    Actions.interface('Lecturer', obj1)

                elif log_choice == '3':
                    Actions.interface('Student', obj1)

                elif log_choice == '0':
                    break

                else:
                    print('Invalid Choice, Try Again')

        elif choice == '0':
            break

        else:
            print('Invalid Choice, Try Again')


print('initializing objects with the data from the given text files')
init_and_menu()
# re-arranged the user's files, way less copy paste code now, way more orginized.
# convertion worked only on my spesific dir, changed it to work globally with os library.
# deletes png files after its done.
