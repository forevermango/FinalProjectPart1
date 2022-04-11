"""
Name: Raahima 
Student ID: 1892523
    
"""

#   Defining Student class
class Student:
    #   Creating constructor
    def __init__(self, ID, last_name, first_name, major, disciplinary_action, gpa, graduation_date):
        self.ID = ID
        self.last_name = last_name
        self.first_name = first_name
        self.major = major
        self.disciplinary_action = disciplinary_action
        self.gpa = gpa
        self.graduation_date = graduation_date
        
    
    #   Defining setter functions
    def set_last_name(self, name):
        self.last_name = name
        
        
    def set_first_name(self, name):
        self.first_name = name
        
        
    def set_major(self, major):
        self.major = major
        
        
    def set_disciplinary_action(self, action):
        self.disciplinary_action = action
        
        
    def set_gpa(self, gpa):
        self.gpa = gpa
        
        
    def set_graduation_date(self, date):
        self.graduation_date = date
    
    #   Defining getter functions
    def get_last_name(self):
        return self.last_name
        
    
    def get_first_name(self):
        return self.first_name
        
    def get_major(self):
        return self.major
        
    
    def get_disciplinary_action(self):
        return self.disciplinary_action
        
    
    def get_gpa(self):
        return self.gpa
        
    
    def get_graduation_date(self):
        return self.graduation_date
    
    
    
    
    
    
    
    
    
    
    
        