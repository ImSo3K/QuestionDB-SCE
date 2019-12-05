class Department:
    def __init__(self, dep_name, coordinator_name):
        self.dep_name = dep_name
        self.coordinator_name = coordinator_name

    def __del__(self):
        print('Dep obj deleted')


