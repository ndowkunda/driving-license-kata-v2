class DrivingLicense:
  
  def __init__(self,data:list):
    self.first_name = data[0]
    self.middle_name = data[1]
    self.surname = data[2]
    self.date_of_birth = data[3]
    self.gender = data[4]
    
  
  def generate_license_number(self) -> str:
    surname = self.surname[0:5]
    birth_decade = self.date_of_birth[9]
    while len(surname) < 5:
      surname +="9"
    return f"{surname.upper()}{birth_decade}"
  
  