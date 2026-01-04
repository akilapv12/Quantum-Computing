# Working with Strings
my_string="Hello World, Akil was here."
my_list=["Hello", "World"]
print("Original:", my_string)
# 👇All of these are methods, they are applied by using the "."

uppercase=my_string.upper()
print(uppercase) # capitalizes all characters

lowercase=my_string.lower()
print(lowercase) # lowercases all characters

stripped=my_string.strip()
print(stripped) # removes whitespace from front and back

replaced=my_string.replace("Akil", "The GOAT")
print(replaced) # replaces specified charachters with new

splitted=my_string.split("o")
print(splitted) # splits variable on specified charachters

joint=":)".join(my_list)
print(joint) # joins iterables with a seperator

starts=my_string.startswith("A") # "starts" is a bool
print(starts) # checks if string starts with ""

ends=my_string.endswith("e")
print(ends) # checks if string ends with ""

found=my_string.find("A")
print(found) # returns index of first occurance of ""

counted=my_string.count("e")
print(counted) # returns no. of times "" occurs

capitalized=my_string.capitalize()
print(capitalized) # Capitalizes first letter and lowers rest

upper=my_string.isupper() # "upper" is a bool
print(upper) # checks if uppercase string

lower=my_string.islower()
print(lower) # checks if lowercase string

my_title=my_string.title()
print(my_title) # capitalizis first letter of each word