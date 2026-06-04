import csv, os, actions

BASE_DIR = os.path.dirname(__file__)#base directory of the project
FILE_NAME = os.path.join(BASE_DIR, "students.csv") #path to the csv file


def export_students_info(data, silent=False):#The function writes the data to the CSV file. The silent parameter=False keeps the "successful" message turned off in order not to show it to the end user when the system exports the data when a student is deleted. The successful message is handled in actions.delete_student() function
    data_in_dict = []
    if data == []:#prevents overwriting the csv file with empty data
        print("\n -> No student data available to export.")
    else:
        try:
            with open(FILE_NAME, 'w', encoding='utf-8', newline='') as file:
                for student in data:
                    data_in_dict.append(student.__dict__)
                    
                headers = data_in_dict[0].keys()
                writer = csv.DictWriter(file, fieldnames=headers)
                writer.writeheader()
                writer.writerows(data_in_dict)
            if not silent:
                print("\nData exported successfully")
        except Exception as ex:
            print(f"\nAn error occurred while exporting the data. Details {ex}")



def import_students_info(students_list):#The function reads the data from CSV file. The silent parameter=False keeps the "successful" message turned off in order not show it to the end user when the system imports the data when it starts for the first time
    try:
        with open(FILE_NAME, 'r', encoding='utf-8',newline='') as file:
            reader = csv.DictReader(file)
            students_list.clear()
            for row in reader:
                #students_list.append(row)
                students_list.append(actions.Student(row["full_name"], row["section"], row["spanish_grade"], row["english_grade"], row["science_grade"], row["social_grade"]))
            print("\nData imported successfully")
    except FileNotFoundError as ex:
        print(f"\nNo exported file found. Please export data first. Details: {ex}")
    except Exception as ex:
        print(f"\nAn error occurred while importing the file. Details: {ex}")

