# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Lora Berger,2024-11-20,Updated Script - added in Functions and Classes
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''

FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
menu_choice: str  # Hold the choice made by the user.
students: list = []  # a table of student data

#Processing Layer
class FileProcessor:
    """
    Collection of functions that will work with JSON files
    """
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """
        This function will read and load data from a JSON file

        :param file_name: string data that contains the name of the JSON file
        :param student_data: list of dictionary rows
        :return: full list of dictionary rows loaded from the JSON file
        """
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except Exception as e:
            message = "Error: There was a problem with reading the file.\n"
            message += "Please check that the file exists and that it is in a json format."
            IO.output_error_messages(message=message,error=e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """
        This function will write data to a JSON file

        :param file_name: string data that contains the name of the JSON file
        :param student_data: list of dictionary rows
        :return: None
        """
        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
            print("The following data was saved to the file!")
            IO.output_student_courses(student_data=student_data)
        except Exception as e:
            if file.closed == False:
                file.close()
            message = "Error: There was a problem with writing to the file.\n"
            message += "Please check that the file is not open by another program."
            IO.output_error_messages(message=message,error=e)

class IO:
    """
    Collection of functions that handles the user input and output
    """
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        This function displays to the user the error messages, both custom and technical

        :param message: message that will be displayed to the user
        :param error: the Exception with technical message to display
        :return: None
        """
        print(message)
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """
        This function displays the menu to the user

        :param menu: string that contains the menu
        :return: None
        """
        print(menu, end='\n\n') #using end parameter to give extra space after menu

    @staticmethod
    def input_menu_choice():
        """
        This function gets the menu choice from the user

        :return: string data of menu choice
        """
        choice = "0"
        try:
            choice = input("What would you like to do: ")
            if choice not in ("1","2","3","4"):
                raise Exception("Please only choose option 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(message=e.__str__())
        return choice

    @staticmethod
    def output_student_courses(student_data: list):
        """
        This function displays the student names and courses to the user

        :param student_data: list of dictionary rows

        :return: None
        """
        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """
        This function requests input from the user to get the student's first and last name and the course
        they are being registered for

        :param student_data: list of dictionary rows

        :return: list
        """
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha(): #checks to make sure only alphabetic characters are used
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha(): #checks to make sure only alphabetic characters are used
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            student_data.append(student)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages(message="One of the inputs was incorrect",error=e)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with your entered data.", error=e)
        return student_data


# Main program script
# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
while True:
    IO.output_menu(menu=MENU)
    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        students = IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_courses(student_data=students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break

print("Program Ended")
