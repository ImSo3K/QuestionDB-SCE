import examSystemData
import UserData
import QuestionAndSolutions


def Lecturer_menu(obj: examSystemData.Exam):
    obj_questions = QuestionAndSolutions.QuestionData(obj)
    print('You can :')
    print('1 - add a question\n2 - display question by Difficulity')
    print('3 - filter the questions shown by criteria')
    print('Press 4 to exit')
    choice = 1
    while 1 <= choice <= 4:
        choice = int(input())

        if choice == 1:
            list_of_values = input('enter with Difficulity, Topic, sub_topic, Code, Format').split()
            obj_questions.add_question(list_of_values)

        if choice == 2:
            obj_questions.print_sorted_question_list_by_diff()

        if choice == 3:
            key = input('enter your filter-by-criteria')
            value = input('enter your filter-by-value')
            obj_questions.print_filtered_question_list(key, value)

        if choice == 4:
            break
