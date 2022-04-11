"""
Name: Raahima 
Student ID: 1892523
    
"""

# importing required modules
import csv
import sys


#   Defining function to read data from a single csv file
def read_csv(filename):
    
    try:
        # initializing the rows list 
        rows = []
        
        # reading csv file
        with open(filename, 'r') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)
            
            # extracting each data row one by one
            for row in csvreader:
                rows.append(row)
                
        return rows
    except:
        print(f"No such file exist with name: {filename}")
        sys.exit()






#   Function to read all csv files
def read_all_inputs(students_data_filename, gpa_filename, graduation_date_filename):
    
    #   READING STUDENTS DATA CSV
    students_data = read_csv(students_data_filename)
    
    #   READING GPA DATA CSV
    gpa_data  = read_csv(gpa_filename)
    
    #   READING GRADUATION DATE DATA CSV
    graduation_date_data = read_csv(graduation_date_filename)
    
    return students_data, gpa_data, graduation_date_data

