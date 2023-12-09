import datetime
class Person(object):
     '''Class to model attributes and methods common to all Persons
    attributes: Name, Password, DOB (date)'''
     def __init__(self, Name=None, DOB_d = None, DOB_m=None, DOB_y=None, Pass=None):
         self.Name = Name 
         self.Password = Pass
         if DOB_d == None or DOB_m == None or DOB_y == None:
             self.DOB = None
         else:
             self.DOB = datetime.date(DOB_y, DOB_m, DOB_d)
         print('init for Person') 
     def __str__(self):
         return 'Name %s was born in %s' %(self.Name, self.DOB)
     def SetDOB(self, Day, Month, Year):
         self.DOB = datetime.date(Year, Month, Day)


class Student(Person):
     '''Class to model attributes and methods 
        common to all Students'''
     def __init__(self, ModulesAndMarks=[]):
         self.ModulesAndMarks = ModulesAndMarks
         super(Student,self).__init__()


class Lecturer(Person):
 '''Class to model attributes and methods common to all Lecturers
     attributes Super Class: Name, Password, DOB (date)
     This class: ModulesToTeach'''
 def __init__(self, Name=None, DOB_d = None, DOB_m=None,DOB_y=None, Pass=None, ModulesToTeach=[]):
      super(Lecturer, self).__init__(Name, DOB_d, DOB_m, DOB_y,Pass)
      self.ModulesToTeach = ModulesToTeach



def print_name_age(alist):
    for p in alist:
        print("Name: {0}, age:{1}".format(p.Name,int((datetime.date.today() - p.DOB).days/365)))
        
