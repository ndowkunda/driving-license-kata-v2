class DrivingLicense:
  
  def generate_license_number(self,data:list) -> str:
    surname = data[2][0:5]
    birth_decade = data[3][9]
    while len(surname) < 5:
      surname +="9"
    return f"{surname.upper()}{birth_decade}"