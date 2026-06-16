import os, data, re


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')    



class Student:
    def __init__(self, name, section, spanish_grade, english_grade, science_grade, social_grade):
        self.name = name
        self.section = section
        self.spanish_grade = spanish_grade
        self.english_grade = english_grade
        self.science_grade = science_grade
        self.social_grade = social_grade


def add_student(list_students):#function collects and validates student data, checks for duplicates, and adds the new student to the list and saves it to the CSV file
    print("\t\t   Add Students\n")
    number_students = is_valid_number_students()
    counter = 1
    while counter <= number_students:
        print(f"\nStudent {counter}")
        print("-"*10)
        full_name = is_valid_name()#calls the function is_valid_name() to validate the full name is not empty or a number
        section = is_valid_section()#calls the function is_valid_section() to validate the section follows the alphanumeric format explicitly (eg. 11B, 11A)
        if check_student_exists(list_students, full_name, section):#calls the function student_exists() to validate the student already exists in the list. It checks against the name and the section
            print("\n ---> Student already exists")
            input("\nPress Enter to return to the main menu...")
            return    #it ends the function to avoid adding the grades in case the student is already in the list
        #the subject grade variables call the function is_valid_grade() to validate the grade is not a string and a number between 0 and 100:
        spanish_grade = is_valid_grade("Spanish")
        english_grade = is_valid_grade("English")
        science_grade = is_valid_grade("Science")
        social_grade = is_valid_grade("Social Studies")
        print("-"*10)
        counter += 1
        # new_student = {#creates new dictionary and saves the data entered by the end user following key:value
        #     "full_name": full_name,
        #     "section": section,
        #     "spanish_grade": spanish_grade,
        #     "english_grade": english_grade, 
        #     "science_grade": science_grade,
        #     "social_grade": social_grade
        # }
        student = Student(full_name, section, spanish_grade, english_grade, science_grade, social_grade)
        list_students.append(student)
        #list_students.append(new_student)#append the dictionary to the list
    #asks the user whether to save the data to the csv file, warning that unsaved data will be lost if not exported later
    save_data = input("\nDo you want to save the student(s) at this point? (y/n): - *If not, remember to export data to local file before login out, otherwise you will lose all data*  -> ").lower()
    while True:
        if save_data == "y":
            data.export_students_info(list_students)
            input("\nPress Enter to return to the main menu...")
            break
        if save_data == "n":
            break
        else:
            print("\nError, please enter 'y' for Yes or 'n' for No")
            save_data = input("Do you want to save the student(s) at this point? y/n: - *If not, remember to export data to local file before login out, otherwise you will lose all data* -> ").lower()


def view_all_students(list_students):#The function shows all the students from the list, showing full name, section, and the subjects' grades
    print("\t\t   All Students\n")
    if list_students == []:# Validates that the list is not empty before processing
        print("\n -> No student data available. Please import data first.")
        input("\nPress Enter to return to the main menu...")
    else:
        for student in list_students:
            # print(f"Full name: {student["full_name"]}")
            # print(f"Section: {student["section"]}")
            # print(f"Spanish grade: {student["spanish_grade"]}")
            # print(f"English grade: {student["english_grade"]}")
            # print(f"Science grade: {student["science_grade"]}")
            # print(f"Social Studies grade: {student["social_grade"]}")

            print(f"Full name: {student.name}")
            print(f"Section: {student.section}")
            print(f"Spanish grade: {student.spanish_grade}")
            print(f"English grade: {student.english_grade}")
            print(f"Science grade: {student.science_grade}")
            print(f"Social Studies grade: {student.social_grade}")
            print("-"*10)
        input("\nPress Enter to return to the main menu...")


def get_top_three_students(list_students):#The function receives the list of all students and sends it to the function get_students_average() to get a list with the students average, it sorts that list and then another list (top_three[]) saves the top 3 students 
    print("\t\t   Top 3 Students\n")
    if list_students == []:# Validates that the list is not empty before processing
        print("\n -> No student data available. Please import data first.")
        input("\nPress Enter to return to the main menu...")
    else:
        print(f"{'  Student':<20} {'Average':<7}")
        print("-"*30)
        list_average = get_students_average(list_students)
        list_average.sort(key=lambda student: student[1], reverse=True)#Sorts the list using the student[1] value (average)
        top_three = list_average[:3]#The top 3 students are saved in a new list
        for student, average in top_three:
            print(f"{student:<20} {average:<10}")
        input("\nPress Enter to return to the main menu...")


def get_overall_average(list_students):#The function receives the list of all students and sends it to the function get_students_average() to get a list with the students average, it shows the name of the student and the average, and then it sums the total of all the averages
    print("\t\t   Overall grade average\n")
    if list_students == []:# Validates that the list is not empty before processing
        print("\n -> No student data available. Please import data first.")
        input("\nPress Enter to return to the main menu...")
    else:
        print(f"{'  Student':<20} {'Average':<7}")
        print("-"*30)
        list_average = get_students_average(list_students)
        sum_of_averages = 0
        counter = 0
        if not list_students == []:#in case the user has not imported the csv file yet and the list is empty, the if prevents a ZeroDivisionError
            for student, average in list_average:
                print(f"{student:<20} {average:<10}")
                sum_of_averages += average
                counter += 1
            print(f"\nTotal average: {sum_of_averages/counter}")
        input("\nPress Enter to return to the main menu...")

    
def get_students_average(list_students):#The function receives the list with all the students and gets their average, then returns a list with the name of the student along with its corresponding average
    list_average = []
    for student in list_students:
        average = (int(student.spanish_grade) + int(student.english_grade) + int(student.science_grade) + int(student.social_grade)) / 4
        list_average.append((student.name, average))
    return list_average


def delete_student(list_students):#the function deletes a student validating both the name and the section
    print("\t\t   Search student to delete\n")
    if list_students == []:# Validates that the list is not empty before processing
        print("\n -> No student data available. Please import data first.")
        input("\nPress Enter to return to the main menu...")
    else:
        full_name = is_valid_name()#calls the function is_valid_name() to validate the full name is not empty or a number
        section = is_valid_section()#calls the function is_valid_section() to validate the section follows the alphanumeric format explicitly (eg. 11B, 11A)
        if check_student_exists(list_students, full_name, section):#calls the function student_exists() to validate the student already exists in the list. It checks against the name and the section
            print(f"\nStudent found: {full_name}, {section}")
            delete_student = input("\n--> Are you sure you want to delete this student? (y/n) ")
            while True:
                if delete_student == 'y':
                    for student in list_students:
                        if student.name == full_name and student.section == section:
                                list_students.remove(student)
                    data.export_students_info(list_students, silent=True)
                    print("\nStudent deleted successfully")
                    input("\nPress Enter to return to the main menu...")
                    break
                if delete_student == 'n':
                    print("\nOperation cancelled. No changes were made.")
                    input("\nPress Enter to return to the main menu...")
                    break
                else:
                    print("\nError, please enter 'y' for Yes or 'n' for No")
                    delete_student = input("\n--> Are you sure you want to delete this student? (y/n)")
        else:
            print("\n --> Student not found. Please check the name and section")
            input("\nPress Enter to return to the main menu...")
        

def get_failed_students(list_students):#the function returns all students that failed at least one subject below 60
    print("\t\t   Failed students\n")
    if list_students == []:# Validates that the list is not empty before processing
        print("\n -> No student data available. Please import data first.")
        input("\nPress Enter to return to the main menu...")
    else:
        failed = False
        for student in list_students:
            if int(student.spanish_grade) < 60 or int(student.english_grade) < 60 or int(student.science_grade) < 60 or int(student.social_grade) < 60: 
                failed = True
                print(f"Name: {student.name}")
                print(f"Section: {student.section}")
                print("Subjects: ")
                if(int(student.spanish_grade)) < 60:
                    print(f"   -Spanish: {student.spanish_grade}")
                if(int(student.english_grade)) < 60:
                    print(f"   -English: {student.english_grade}")
                if (int(student.science_grade)) < 60:
                    print(f"   -Science: {student.science_grade}")
                if(int(student.social_grade)) < 60:
                    print(f"   -Social Studies: {student.social_grade}") 
                print("-"*10)
        input("\nPress Enter to return to the main menu...")
        if not failed:
            print("\n --> No failed students found")
            input("\nPress Enter to return to the main menu...")


def is_valid_name():#Prompts the user for a full name and validates it contains only letters and spaces
    while True:
        full_name = input("Full name: ").title()
        if not full_name.replace(" ", "").isalpha():
            print("Name cannot be empty or contain numbers")
        else:
            return full_name


def is_valid_section():#the function uses regex to validate the section follows the format of 2 digits and 1 letter (e.g. 11A, 10B)
    while True:
        section = input("Section: ").upper()
        if re.match(r'^\d{1,2}[A-Za-z]$', section):#validates the section starts with either 1 or 2 numbers followed by a letter
            return section
        else:
            print("Invalid section. It must contain both numbers and letters (e.g. 11A, 11B)")


def is_valid_grade(subject):#Prompts the user for a grade and validates it is a number between 0 and 100
    while True:
        try:
            grade = int(input(f"{subject} grade (0-100): "))
            if grade >= 0 and grade <= 100:
                return grade
            else:
                print("Grade must be a number between 0 and 100")
        except ValueError as ex:
            print(f"Grade must be a number between 0 and 100. Details {ex}")


def is_valid_number_students():#Prompts the user for the number of students to add and validates it is a positive integer greater than 0
    while True:
        try:
            number_student = int(input("How many students do you want to add: "))
            if number_student > 0:
                return number_student
            else:
                print("Number of students must be grater than 0")
        except ValueError as ex:
            print(f"Error, enter a valid number. Details: {ex}\n")


def check_student_exists(list_students, full_name, section): #function receives the list, and the name/section of the student to validate if already exists
    for student in list_students:
        if full_name == student.name and section == student.section:
            return True
    return False



        