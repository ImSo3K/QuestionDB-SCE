class UserData:
    def __init__(self):
        self.lecturer_list = []

    def add_lecturer(self, lecturer_first_name='', lecturer_last_name=''):
        self.lecturer_list.append((lecturer_first_name, lecturer_last_name))

    def edit_lecturer_info(self, lecturer_first_name='', lecturer_edit=''):
        for i, name in enumerate(self.lecturer_list):
            if lecturer_first_name == name[0]:
                self.lecturer_list.insert(i, lecturer_edit)
