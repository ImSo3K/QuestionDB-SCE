import examSystemData


def get_exam_info(obj: examSystemData.Exam):
    with open('Exams.txt') as f:
        line = f.read().split()
    obj.exam_date = line[0]
    obj.exam_semester = line[1]


def get_question_info(obj: examSystemData.Exam):
    with open('Questions.txt') as f:
        for line in f:
            if not line.strip():
                break
            line = line.split()
            i = 0
            for key in obj.question.question_info.keys():
                obj.question.question_info[key] = line[i]
                i += 1
            obj.question_list.append(obj.question)
