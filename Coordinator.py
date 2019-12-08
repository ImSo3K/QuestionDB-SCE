import examSystemData
import UserData
import QuestionAndSolutions


def main():
    pass


def Coordinator_menu(obj: examSystemData.Exam):
    obj_user_data = UserData.UserData()
    obj_questions = QuestionAndSolutions.QuestionData(obj)
    obj_solutions = QuestionAndSolutions.SolutionData()
    print('You can :')
    print('1 - add a lecturer to the system\n2 - edit lecturer info')
    print('3 - add a solution\n4 - add a question')
    print('5 - edit a question\n6 - display question by Difficulity')
    print('7 - filter the questions shown by criteria')
    print('Press 8 to exit')
    choice = 1
    while 1 <= choice <= 7:
        choice = int(input())
        if choice == 1:
            lecturer_first_name, lecturer_last_name = input(
                'enter lecturer first name + last name with a whitespace between').split()
            obj_user_data.add_lecturer(lecturer_first_name, lecturer_last_name)

        if choice == 2:
            lecturer_first_name, lecturer_name_change = input(
                'enter lecturer first name + the change with a whitespace between').split()
            obj_user_data.edit_lecturer_info(lecturer_first_name, lecturer_name_change)

        if choice == 3:
            obj_solutions.add_sol(input('Add A solution'))

        if choice == 4:
            list_of_values = input('enter withDifficulity, Topic, sub_topic, Code, Format').split()
            obj_questions.add_question(list_of_values)

        if choice == 5:
            key = input('enter what you want to change, Difficulity, Topic, sub_topic, Code, Format')
            value = input('enter your new value')
            obj_questions.edit_question(key, value)

        if choice == 6:
            obj_questions.print_sorted_question_list_by_diff()

        if choice == 7:
            key = input('enter your filter-by-criteria')
            value = input('enter your filter-by-value')
            obj_questions.print_filtered_question_list(key, value)

        if choice == 8:
            break


if __name__ == "__main__":
    main()
