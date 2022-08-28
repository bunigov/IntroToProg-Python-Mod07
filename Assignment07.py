# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Demonstrating how Pickling and Structured Error Handling works
# ChangeLog (Who,When,What):
# BorisU,8/22/2022,Created script
# ---------------------------------------------------------------------------- #
import pickle
import os  #for current directory

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
table_list = []   # A list that acts as a 'table' of rows
#row_dict = {}     # A row of data separated into elements of a dictionary
choice_str = ""   # Captures user option selection

# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def add_data_to_list(task_to_add, priority, list_of_rows):
        """ Adds data to a list of dictionary rows

        :param task_to_add: (string) with name of task:
        :param priority: (string) with name of priority:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        row = {"Task": str(task_to_add).strip(), "Priority": str(priority).strip()}
        list_of_rows.append(row)
        return list_of_rows

    @staticmethod
    def remove_data_from_list(task_to_remove, list_of_rows):
        """ Removes data from a list of dictionary rows

        :param task_to_remove: (string) with name of task:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows, (bool) status of removal
        """
        status = False
        for row in list_of_rows:
            task, priority = dict(row).values()
            if task == task_to_remove:
                list_of_rows.remove(row)
                status = True

        return list_of_rows, status

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input(bcolors.BOLD + bcolors.OKBLUE + "Which option would you like to perform? [1 to 5] - "
                           + bcolors.ENDC + bcolors.ENDC)).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def input_new_task_and_priority():
        """  Gets task and priority values to be added to the list

        :return: (string, string) with task and priority
        """
        task = str(input(bcolors.BOLD + bcolors.OKBLUE +"What is the task you want to add? - "+ bcolors.ENDC + bcolors.ENDC)).strip().capitalize()
        priority = str(input(bcolors.BOLD + bcolors.OKBLUE +"What is task's priority? [high|medium|low] - "+ bcolors.ENDC + bcolors.ENDC)).strip().capitalize()
        return task, priority

    @staticmethod
    def input_task_to_remove():
        """  Gets the task name to be removed from the list

        :return: (string) with task
        """
        TaskToRemove = input(bcolors.BOLD + bcolors.OKBLUE + "Which TASK would you like removed? - " + bcolors.ENDC)
        return TaskToRemove

    @staticmethod
    def input_pickle_to_save_to():
        """  Gets the name of the pick file to load to

        :return: (string) file to save to (with extension)
        """
        file_name_to_save_to = input(bcolors.OKBLUE + "Please enter the name and extension of file you want to SAVE to.. (e.g. AppData.dat) " + bcolors.ENDC)
        return file_name_to_save_to

    @staticmethod
    def input_pickle_to_load_from():
        """  Gets the name of the pickle file to load from

        :return: (string) file to load from (with extension)
        """
        file_name_to_load_from = input(bcolors.OKBLUE + "Please enter the name and extension of file you want to LOAD from.. (e.g. AppData.dat) " + bcolors.ENDC)
        return file_name_to_load_from

    @staticmethod
    def output_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Please select from \u001b[1mMenu of Options\u001b[0m
        1) \x1B[4mSee\x1B[0m Data in List  
        2) \x1B[4mAdd\x1B[0m Data (Task/Priority) to List
        3) \x1B[4mRemove\x1B[0m Row (Task/Priority) from List
        4) \x1B[4mLoad\x1B[0m Data from Pickle File
        5) \x1B[4mSave\x1B[0m Data to Pickle File
        6) \x1B[4mExit\x1B[0m Program
        ''')
        print()  # Add an extra line for looks
        #

    @staticmethod
    def output_current_tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print(bcolors.OKBLUE + "Here's the current list ..." + bcolors.ENDC)
        #print()  # Add an extra line for looks
        # print(bcolors.BOLD + "************ Current ToDo List ************ " + bcolors.ENDC)
        print("Task " + "|" + " Priority")
        for row in list_of_rows:
            print(row["Task"] + " | " + row["Priority"] + "")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def output_successful_task_removal():
        """ Display output of successful data removal

            :return: nothing
            """
        print(bcolors.OKGREEN + "****Task " + task + " was succesfully removed. Displaying updated list contents...****" + bcolors.ENDC)

    @staticmethod
    def output_failed_task_removal():
        """ Display output of failed data removal

            :return: nothing
            """
        print(bcolors.FAIL + "****Task " + task + " not found. Please enter a valid task to remove.****" +bcolors.ENDC)

    @staticmethod
    def output_successful_program_exit():
        """ Display output of requested user exit

            :return: nothing
            """
        print(bcolors.OKBLUE + "****Exiting... Goodbye...***" + bcolors.ENDC)

    @staticmethod
    def output_list_is_empty():
        """ Display output informing user that list is empty
            :return: nothing
            """
        print(bcolors.OKBLUE + "List is currently empty. Please add task to the list. \n"
              + bcolors.ENDC )  # bolded and blue

    @staticmethod
    def output_task_added():
        """ Display output informing user task was added
            :return: nothing
            """
        print(bcolors.OKGREEN + "Task was successfully added.  Displaying updated list contents...\n"
              + bcolors.ENDC )  # bolded and blue

    @staticmethod
    def output_successful_data_load_pickle_to_memory(file, objData):
        """ Display output informing user of successful data load from pickle file to memory
            :return: nothing
            """
        print(bcolors.OKGREEN + "Data loaded to Memory from Pickle file " + file + ". \n" + bcolors.ENDC)  # bolded
        print("Raw Data:")
        print(objData)
        print('\n')

    @staticmethod
    def output_successful_data_load_memory_to_list():
        """ Display output informing user of successful data load from memory to list
            :return: nothing
            """
        print(bcolors.OKGREEN + "Data loaded to List from Memory" + ".\n" + bcolors.ENDC)  # bolded
        print(bcolors.OKGREEN + "Fetching updated list..." + ".\n" + bcolors.ENDC)  # bolded
        print('\n')

    @staticmethod
    def output_error_no_such_file_to_load():
        """ Display output informing user of their attempt to load a file that doesn't exist in the directory
            :return: nothing
            """
        print(
            bcolors.FAIL + "No such file exists in current directory. Please provide a valid existing file. " + bcolors.ENDC)

    @staticmethod
    def output_error_attempting_to_save_empty_list():
        """ Display output informing user of their attempt to save empty list to a pickle file
            :return: nothing
            """
        print(bcolors.FAIL + "List is empty. Nothing to save. " + bcolors.ENDC)

    @staticmethod
    def output_error_user_selected_invalid_option():
        """ Display output informing user that they have selected an invalid menu option
            :return: nothing
            """
        print(bcolors.FAIL + "Invalid Option. Please select a valid option from the menu. " + bcolors.ENDC)

    @staticmethod
    def output_welcome_banner():
        """ Display welcome banner to the user
            :return: nothing
            """
        print(bcolors.HEADER + "Welcome to the Task Organizer App!!! " + bcolors.ENDC)  # runs only once

class bcolors:  #for simplifying color display of messages
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Main Body of Script  ------------------------------------------------------ #
IO.output_welcome_banner()

while (True): #continues dont seem to be needed, only need break since loop will continue
    IO.output_menu_tasks()  # Shows menu
    choice_str = IO.input_menu_choice()  # Get menu option

    #See data currently in the list - read only
    if choice_str.strip() == '1' or choice_str.strip().lower() == 'see':
        if len(table_list) ==0:  #empty list, want to show message and not list contents
            IO.output_list_is_empty()
        else:  #if list has data

            IO.output_current_tasks_in_list(list_of_rows=table_list)  # Show current data in the list/table

        #continue

    #Add data to the list - write
    elif choice_str.strip() == '2' or choice_str.strip().lower() == 'add':
        task, priority = IO.input_new_task_and_priority()
        table_lst = Processor.add_data_to_list(task_to_add=task, priority=priority, list_of_rows=table_list)
        IO.output_task_added()
        IO.output_current_tasks_in_list(list_of_rows=table_list)  #show the updated contents of the list

    #Remove data from the list - write
    elif choice_str.strip() == '3' or choice_str.strip().lower() == 'remove' or choice_str.strip().lower() == 'delete':
        IO.output_current_tasks_in_list(list_of_rows=table_list)  # Show current data in the list/table
        task = IO.input_task_to_remove()
        table_lst, status = Processor.remove_data_from_list(task_to_remove=task, list_of_rows=table_list)
        if (status == True):
            IO.output_successful_task_removal()
        else:
            IO.output_failed_task_removal()
        IO.output_current_tasks_in_list(list_of_rows=table_list)  #show updated list contents
        #continue  # to show the menu

    #Retrieve/load data from Pickle file, load back into the list
    elif choice_str.strip() == '4' or choice_str.strip().lower() == 'load':
        strFileToLoadFrom = IO.input_pickle_to_load_from()
        try:
            with open(strFileToLoadFrom, "rb") as input_file:
                objFileData = pickle.load(input_file)  #automatic close        input_file.close()

            IO.output_successful_data_load_pickle_to_memory(file = strFileToLoadFrom, objData = objFileData)

            #Processor.load_pickle_into_list
            # load back into the list
            for elem in objFileData:
                row = {"Task": elem["Task"], "Priority": elem["Priority"]}  # generate a dictionary
                table_list.append(row)  # change to function and to use list of rows later

            IO.output_successful_data_load_memory_to_list()
            IO.output_current_tasks_in_list(list_of_rows=table_list)

        except FileNotFoundError:
            IO.output_error_no_such_file_to_load()

        #finally:

    #Save data to Pickle file
    elif choice_str.strip() == '5' or choice_str.strip().lower() == 'save':
        if len(table_list) == 0:
            IO.output_error_attempting_to_save_empty_list()
        else:
            strFileToSaveTo = IO.input_pickle_to_save_to()
            with open(strFileToSaveTo, "wb") as output_file:  #intentionally want to create new file each time
                pickle.dump(table_list, output_file)  #automatic close        output_file.close()
            print(bcolors.OKGREEN + "Data Saved to Pickle file " + strFileToSaveTo  + ". \n" + bcolors.ENDC)  # bolded
            print(bcolors.BOLD + "Pickle File Located at " + bcolors.ENDC + os.getcwd() + "\\" + strFileToSaveTo)

    # Exit Program
    elif choice_str.strip() == '6' or choice_str.strip().lower() == 'exit' or choice_str.strip().lower() == 'x':
        IO.output_successful_program_exit()
        break  # by exiting loop

    # Invalid Input Option:  User Enters an invalid option from the menu
    else:
        IO.output_error_user_selected_invalid_option()



# Present user with options
# Get user input
# Create a list of tasks and priorities
# Save to a pickle file
# Load from pickle file to memory
# Show error handling by providing invalid file to read
# Make changes to the list
# Show error handling by providing invalid input
# Save pickle again with the changes
# Load updated pickle again to validate the changes