full_dot = '●'
empty_dot = '○'

def create_character(character_name, strength, intelligence, charisma):
    if not isinstance(character_name, str):
        print("The character name should be a string.")
    if character_name=="":
        print("The character should have a name.")
    if len(character_name)>10:
        print("The character name is too long.")
    if " " in character_name:
        print("The character name should not contain spaces.")
    if not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
        print("All stats should be integers.")
    if strength < 1 or intelligence < 1 or charisma < 1:
        print("All stats should be no less than 1.")
    if strength > 4 or intelligence > 4 or charisma > 4:
        print("All stats should be no more than 4.")
    if strength + intelligence + charisma != 7:
        print("The character should start with 7 points.")
    print(character_name)
    print("STR", strength*"●" + (10-strength)*"○")
    print("INT", intelligence*"●" + (10-intelligence)*"○")
    print("CHA", charisma*"●" + (10-charisma)*"○")

character_name = input("Enter character name: ")
strength = int(input("Strength: "))
intelligence = int(input("Intelligence: "))
charisma = int(input("Charisma: "))

create_character(character_name, strength, intelligence, charisma)