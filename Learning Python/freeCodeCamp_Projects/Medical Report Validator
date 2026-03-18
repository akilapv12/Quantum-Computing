# Medical Report Validator
print("This is a Medical Report Validator.")
print("But it validates based on a specific format made by me.")
print("It will say your report is invalid if it doesnt follow my format.")
print("So I dont sugest it for actual use.")
print("\nTo check my code you can use this valid report:")
print("[{'patient_id': 'P1001', 'age': 34, 'gender': 'Female', 'diagnosis': 'Hypertension', 'medications': ['Lisinopril'], 'last_visit_id': 'V2301'}, {'patient_id': 'p1002', 'age': 47, 'gender': 'male', 'diagnosis': 'Type 2 Diabetes', 'medications': ['Metformin', 'Insulin'], 'last_visit_id': 'v2302'}, {'patient_id': 'P1003', 'age': 29, 'gender': 'female', 'diagnosis': 'Asthma', 'medications': ['Albuterol'], 'last_visit_id': 'v2303'}, {'patient_id': 'p1004', 'age': 56, 'gender': 'Male', 'diagnosis': 'Chronic Back Pain', 'medications': ['Ibuprofen', 'Physical Therapy'], 'last_visit_id': 'V2304'}]")
print("Feel free to edit it to check if my code returns False when report is invalid.")
print(" ")
print(" ")
# example report:

# medical_records = [
#     {
#         'patient_id': 'P1001',
#         'age': 34,
#         'gender': 'Female',
#         'diagnosis': 'Hypertension',
#         'medications': ['Lisinopril'],
#         'last_visit_id': 'V2301',
#     },
#     {
#        'patient_id': 'p1002',
#        'age': 47,
#         'gender': 'male',
#         'diagnosis': 'Type 2 Diabetes',
#         'medications': ['Metformin', 'Insulin'],
#         'last_visit_id': 'v2302',
#     },
#     {
#         'patient_id': 'P1003',
#         'age': 29,
#         'gender': 'female',
#         'diagnosis': 'Asthma',
#         'medications': ['Albuterol'],
#         'last_visit_id': 'v2303',
#     },
#     {
#         'patient_id': 'p1004',
#         'age': 56,
#         'gender': 'Male',
#         'diagnosis': 'Chronic Back Pain',
#         'medications': ['Ibuprofen', 'Physical Therapy'],
#         'last_visit_id': 'V2304',
#     }
# ]

import re

import ast  # Abstract Syntax Trees Module,  to safely convert string input to Python object

# Get user input as a string
user_input = input("Enter your medical records as a Python list of dictionaries:\n")

try:
    # Convert string input to Python object
    medical_records = ast.literal_eval(user_input) # evaluates string to list
except Exception as e: # 'Exception' is a class in python for all errors, this error is stored in variable 'e'
    print("Invalid input:", e)
    medical_records = []  

def find_invalid_records(
    patient_id, age, gender, diagnosis, medications, last_visit_id
):
    constraints = {
        'patient_id': isinstance(patient_id, str)
        and re.fullmatch('p\d+', patient_id, re.IGNORECASE),
        'age': isinstance(age, int) and age >= 18,
        'gender': isinstance(gender, str) and gender.lower() in ('male', 'female'),
        'diagnosis': isinstance(diagnosis, str) or diagnosis is None,
        'medications': isinstance(medications, list)
        and all([isinstance(i, str) for i in medications]),
        'last_visit_id': isinstance(last_visit_id, str)
        and re.fullmatch('v\d+', last_visit_id, re.IGNORECASE)
    }
    return [key for key, value in constraints.items() if not value]

def validate(data):

    if len(data) == 0:
        print("Invalid format: list is empty.")
        return False

    is_sequence = isinstance(data, (list, tuple))

    if not is_sequence:
        print('Invalid format: expected a list or tuple.')
        return False
        
    is_invalid = False
    key_set = set(
        ['patient_id', 'age', 'gender', 'diagnosis', 'medications', 'last_visit_id']
    )

    for index, dictionary in enumerate(data):
        if not isinstance(dictionary, dict):
            print(f'Invalid format: expected a dictionary at position {index}.')
            is_invalid = True
            continue

        if set(dictionary.keys()) != key_set:
            print(
                f'Invalid format: {dictionary} at position {index} has missing and/or invalid keys.'
            )
            is_invalid = True
            continue

        invalid_records = find_invalid_records(**dictionary)

        if invalid_records:
            print(f'Invalid fields in record {index}: {invalid_records}')
            is_invalid = True
        

    if is_invalid:
        return False
    print('Valid format.')
    return True

validate(medical_records)