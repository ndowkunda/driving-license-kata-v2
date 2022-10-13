from inspect import Parameter
import pytest
from driving_license_kata.driving_license import DrivingLicense


testcases = [(["John","James","Smith","01-Jan-2000","M"],"SMITH"),
             (["John","James","Smit","01-Jan-2000","M"],"SMIT9"),
             (["John","James","Smithers","01-Jan-2000","M"],"SMITH")]

testcases_birth_decade = [ (["John","James","Smith","01-Jan-2000","M"],"0"),
             (["John","James","Smith","01-Jan-1990","M"],"9"),
             (["John","James","Smith","01-Jan-1980","M"],"8")]

class TestDrivingLicenseGenerator:
  
  @pytest.mark.parametrize("test_input,expected",testcases)
  def test_returns_surname_in_first_5_chars(self,test_input,expected):
    driving_license = DrivingLicense(test_input)
    driving_license_number = driving_license.generate_license_number()
    surname = driving_license_number[0:5]
    assert surname == expected

  @pytest.mark.parametrize("data_input,expected",testcases_birth_decade)
  def test_returns_decade_number_from_birth_year_at_sixth_char(self,data_input,expected):
    driving_license = DrivingLicense(data_input)
    driving_license_number = driving_license.generate_license_number()
    birth_decade = driving_license_number[5]
    assert birth_decade == expected
