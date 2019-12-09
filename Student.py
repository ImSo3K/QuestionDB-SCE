import examSystemData
import QuestionAndSolutions


def Student_menu(obj: examSystemData.Exam):
    obj_questions = QuestionAndSolutions.QuestionData(obj)
    print('You can :')
    print('1 - display question by Difficulity')
    print('2 - filter the questions shown by criteria')
    print('Press 3 to exit')
    choice = 1
    while 1 <= choice <= 3:
        choice = int(input())
        if choice == 1:
            obj_questions.print_sorted_question_list_by_diff()

        if choice == 2:
            key = input('enter your filter-by-criteria')
            value = input('enter your filter-by-value')
            obj_questions.print_filtered_question_list(key, value)

        if choice == 3:
            break
