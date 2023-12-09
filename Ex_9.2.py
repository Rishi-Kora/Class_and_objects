import datetime
class Person(object):
     '''Class to model attributes and methods common to all Persons
    attributes: Name, Password, DOB (date)'''
     def __init__(self, Name=None, DOB_d = None, DOB_m=None, DOB_y=None, Pass=None):
         self.Name = Name 
         self.Password = Pass
         self.DOB = datetime.date(DOB_y, DOB_m, DOB_d)
         print('init for Person') 
     def __str__(self):
         return 'Name %s was born in %s' %(self.Name, self.DOB)
     def SetDOB(self, Day, Month, Year):
         self.DOB = datetime.date(Year, Month, Day)


class Student(Person):
     '''Class to model attributes and methods 
        common to all Students'''
     def __init__(self, ModuleAndMarks=[],Name=None, DOB_d = None, DOB_m=None, DOB_y=None, Pass=None):
         self.ModuleAndMarks = ModuleAndMarks
         super(Student,self).__init__(Name,DOB_d,DOB_m,DOB_y,Pass)
         
