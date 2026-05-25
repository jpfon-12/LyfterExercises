
import menu, actions, data


def main():
    students = []#memory list that stores all student records during the program's execution
    data.import_students_info(students, silent=True)#Loads existing student data from CSV into memory before any user interaction begins
    menu.show_menu(students)# Launches the main menu and starts the program flow


if __name__ == "__main__":
    main()
    