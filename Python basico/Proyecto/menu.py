import actions, data, time

def show_menu(list_students):
    while True:
        try:    
            print("\n\t *** Student Management System *** \n")
            print("\t\t   Main Menu\n")
            print("1. Add student")
            print("2. View all students")
            print("3. View top 3 students")
            print("4. View overall grade average")
            print("5. Delete student")
            print("6. View failed students")
            print("7. Export data to CSV")
            print("8. Import data to CSV")
            print("0. Exit")
            print("="*20)
            option = int(input("Select an option: "))
        
            match option:#Displays the main menu and handles user navigation throughout the program
                case 1:
                    actions.clear_console()
                    actions.add_student(list_students)
                    actions.clear_console()
                case 2:
                    actions.clear_console()
                    actions.view_all_students(list_students)
                    actions.clear_console()
                case 3:
                    actions.clear_console()
                    actions.get_top_three_students(list_students)
                    actions.clear_console()
                case 4:
                    actions.clear_console()
                    actions.get_overall_average(list_students)
                    actions.clear_console()
                case 5:
                    actions.clear_console()
                    actions.delete_student(list_students)
                    actions.clear_console()
                case 6:
                    actions.clear_console()
                    actions.get_failed_students(list_students)
                    actions.clear_console()
                case 7:
                    actions.clear_console()
                    data.export_students_info(list_students)
                    input("\nPress Enter to return to the main menu...")
                    actions.clear_console()
                case 8:
                    actions.clear_console()
                    data.import_students_info(list_students)
                    input("\nPress Enter to return to the main menu...")
                    actions.clear_console()
                case 0:
                    print("\n--> Exiting the system...")
                    time.sleep(2)
                    break
                case _:
                    print("\n --> Invalid option. Please select a valid option from the menu.")
        except ValueError as ex:
            print(f"\n --> Error. Please enter a number from the menu. Details: {ex}")            


    