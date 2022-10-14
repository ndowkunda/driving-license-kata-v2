class DrivingLicense:

    def __init__(self, data: list):
        self.first_name = data[0]
        self.middle_name = data[1]
        self.surname = data[2]
        self.date_of_birth = data[3]
        self.gender = data[4]

    def generate_license_number(self) -> str:
        formatted_birth_decade = self.__format_birth_decade()
        formatted_surname = self.__format_surname()
        return f"{formatted_surname}{formatted_birth_decade}"

    def __format_birth_decade(self) -> str:
        return self.date_of_birth[9]

    def __format_surname(self) -> str:
        surname = self.surname[0:5]
        while len(surname) < 5:
            surname += "9"
        return surname.upper()
