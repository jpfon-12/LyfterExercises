import csv

def export_students_info(data, silent=False):#The function writes the data to the CSV file. The silent parameter=False keeps the "successful" message turned off in order not show it to the end user when the system export the data when a student is deleted. The successful message is handled in actions.delete_student() function
    try:
        with open("Python basico\Proyecto\students.csv", 'w', encoding='utf-8', newline='') as file:
            headers = data[0].keys()
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)
        if not silent:
            print("\nData exported successfully")
    except Exception as ex:
        print(f"\nAn error occurred while exporting the data. Details {ex}")



def import_students_info(students_list, silent=False):#The function reads the data from CSV file. The silent parameter=False keeps the "successful" message turned off in order not show it to the end user when the system imports the data when it starts for the first time
    try:
        with open("Python basico\Proyecto\students.csv" , 'r', encoding='utf-8',newline='') as file:
            reader = csv.DictReader(file)
            students_list.clear()
            for row in reader:
                students_list.append(row)
        if not silent:
            print("\nData imported successfully")
    except FileNotFoundError as ex:
        print(f"\nNo exported file found. Please export data first. Details: {ex}")
    except Exception as ex:
        print(f"\nAn error occurred while importing the file. Details: {ex}")

