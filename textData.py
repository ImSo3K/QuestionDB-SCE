import examSystemData

def get_department_list(obj):
    fo_dep = open('Departments.txt', 'r')
    line = fo_dep.readline().rstrip()
    obj.dep_name = line
    line = fo_dep.readline().rstrip()
    obj.coordinator_name = line
    fo_dep.close()

