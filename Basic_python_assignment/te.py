import datetime
import json

my_dict = {}

def write_json(my_dict, filename = 'data.json'):
    with open(filename, 'a') as file:
        json.dump(my_dict, file)  

def validate_DOB(DOB):
    try:
        datetime.datetime.strptime(DOB, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Format mis-matched, it must be in format YYYY-MM-DD")
    
def validate_age(age):
    try:
        age.isdigit()
    except ValueError:
        raise ValueError("Age must be numberic")
    
def validate_string(chkstring):
    try:
        isinstance(chkstring, str)
    except ValueError:
        raise ValueError("Input must be String")
        
name = input("Enter your name:")
validate_string(name)
my_dict['Name'] = name

DOB = input("Enter your Date of Birth:")
validate_DOB(DOB)
my_dict['DOB'] = DOB

age = input("Enter your age:")
validate_age(age)
my_dict['age'] = age

print("Enter 3 list of your hobbies:")
hobbies = []
for x in range(3):
    y = input()
    validate_string(y)
    hobbies.append(y)
my_dict['Hobbies'] = hobbies   
write_json(my_dict)