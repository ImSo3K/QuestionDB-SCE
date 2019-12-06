def get_exam_info(obj):
    with open('Exams.txt') as f:
        line = f.read().split()
    obj.exam_date = line[0]
    obj.exam_semester = line[1]
