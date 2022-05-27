

class Student:
    school="AkiraChix"
    
    def __init__(self,first_name,last_name,age,country):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.country=country
        
 
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
        
    def get_initial(self):
        return f"{self.first_name[0].split()} {self.last_name[0].split()}"

    def greeting(self):
      return f"Hello {self.first_name} {self.last_name} from {self.country}, welcome to {self.school}"


    def year_of_birth(self,current_year):
         self.current_year=current_year
         return self.current_year-self.age


