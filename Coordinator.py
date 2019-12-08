import examSystemData


def Coordinator_menu():
    print('You can :')
    print('1 - add a lecturer to the system\n2 - edit lecturer info')
    print('3 - add a solution\n4 - edit a question')
    print('5 - display a question\n6 - filter the questions shown by criteria')
    print('Press 6 to exit')
    choice = 0
    while 0 <= choice <= 6:
        choice = int(input())
        if choice == 1:
            input('')


if __name__ == "__main__":
    Coordinator_menu()
