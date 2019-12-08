import examSystemData


class QuestionData:
    def __init__(self, obj: examSystemData.Exam):
        self.question_database = obj.question_list

    def add_question(self, list_of_values: list):
        empty_question = examSystemData.Question()
        for key in empty_question.question_info.keys():
            empty_question.question_info[key] = list_of_values[0]
            list_of_values = list_of_values[1:]
        self.question_database.append(empty_question)

    def edit_question(self, v_key='', v_value=''):
        for i in enumerate(self.question_database):
            obj = examSystemData.Question()
            obj.question_info = self.question_database[i]
            for key in obj.question_info.keys():
                if key == v_key:
                    obj.question_info[key] = v_value

    def print_sorted_question_list_by_diff(self):
        print(sorted(self.question_database, key=lambda i: i['Difficulity']))

    def print_filtered_question_list(self, v_key='', v_value=''):
        for i in enumerate(self.question_database):
            obj = examSystemData.Question()
            obj.question_info = self.question_database[i]
            for key, value in obj.question_info.items():
                if key == v_key and value == v_value:
                    examSystemData.Question.print_question_info(self.question_database[i])


class SolutionData:
    def __init__(self):
        self.solution_list = []

    def add_sol(self, sol=''):
        self.solution_list.append(sol)
