# User Configuration Manager

# Example settings:
# test_settings = {
#     'theme':'dark',
#     'language':'english',
#     'notifications':'enabled'
# }

import ast
user_input = input("Enter your current settings: ")
try:
    test_settings = ast.literal_eval(user_input)
    if not isinstance(test_settings, dict):
        print("Input is not a dictionary. Starting with empty settings.")
        test_settings = {}
except Exception as e:
    print("Invalid input:", e)
    test_settings = {}  

user = input("Would you like to add/update/delete/view settings: ").lower()

def add_setting(settings, pair):
    key, value = pair
    key = key.lower()
    value = value.lower()
    if key in settings.keys():
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        settings[key]=value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings, pair):
    key, value = pair
    key = key.lower()
    value = value.lower()
    if key in settings.keys():
        settings[key]=value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings, key):
    key = key.lower()
    if key in settings.keys():
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return f"Setting not found!"

def view_settings(settings):
    if not settings:
        return f"No settings available."
    else:
        result = "Current User Settings:\n"
        for key, value in settings.items():
            result += f"{key.capitalize()}: {value}\n"
        return result

if user=="add":
    key = input("Enter the key of settings you want to add: ")
    value = input("Enter the value of the settings you want to add: ")
    pair = (key, value)
    print(add_setting(test_settings, pair))
elif user=="update":
    key = input("Enter the key of settings you want to update: ")
    value = input("Enter the new value of the settings you want to update: ")
    pair = (key, value)
    print(update_setting(test_settings, pair))
elif user=="delete":
    key = input("Enter the key of settings you want to delete: ")
    print(delete_setting(test_settings, key))
elif user=="view":
    print(view_settings(test_settings))
else:    
    print("Invalid option! Please choose add, update, delete, or view.")