# Hangman

import random
import sys

stage_0 = '''
  |---------|
  |         |
  |       
  |       
  |       
  |                          
_____
_____
''' 

stage_1 = '''
  |---------|
  |         |
  |         O
  |    
  |     
  |                          
_____
_____
''' 

stage_2 = '''
  |---------|
  |         |
  |         O
  |         | 
  |        
  |                          
_____
_____
''' 

stage_3 = '''
  |---------|
  |         |
  |         O
  |         | \\
  |         
  |                          
_____
_____
''' 

stage_4 = '''
  |---------|
  |         |
  |         O
  |       / | \\
  |         
  |                          
_____
_____
''' 

stage_5 = '''
  |---------|
  |         |
  |         O
  |       / | \\
  |          \\ 
  |                          
_____
_____
''' 

stage_6 = '''
  |---------|
  |         |
  |         O
  |       / | \\
  |        / \\ 
  |                          
_____
_____
''' 

stages = [stage_0, stage_1, stage_2, stage_3, stage_4, stage_5, stage_6]

safe = '''
   O
  /|\\
  / \\
'''

country_list = [
    "AFGHANISTAN", "ALBANIA", "ALGERIA", "ANDORRA", "ANGOLA", 
    "ANTIGUA AND BARBUDA", "ARGENTINA", "ARMENIA", "AUSTRALIA", "AUSTRIA", 
    "AZERBAIJAN", "BAHAMAS", "BAHRAIN", "BANGLADESH", "BARBADOS", 
    "BELARUS", "BELGIUM", "BELIZE", "BENIN", "BHUTAN", 
    "BOLIVIA", "BOSNIA AND HERZEGOVINA", "BOTSWANA", "BRAZIL", "BRUNEI", 
    "BULGARIA", "BURKINA FASO", "BURUNDI", "CABO VERDE", "CAMBODIA", 
    "CAMEROON", "CANADA", "CENTRAL AFRICAN REPUBLIC", "CHAD", "CHILE", 
    "CHINA", "COLOMBIA", "COMOROS", "CONGO", "COSTA RICA", 
    "COTE D IVOIRE", "CROATIA", "CUBA", "CYPRUS", "CZECH REPUBLIC", 
    "DEMOCRATIC REPUBLIC OF THE CONGO", "DENMARK", "DJIBOUTI", "DOMINICA", "DOMINICAN REPUBLIC", 
    "ECUADOR", "EGYPT", "EL SALVADOR", "EQUATORIAL GUINEA", "ERITREA", 
    "ESTONIA", "ESWATINI", "ETHIOPIA", "FIJI", "FINLAND", 
    "FRANCE", "GABON", "GAMBIA", "GEORGIA", "GERMANY", 
    "GHANA", "GREECE", "GRENADA", "GUATEMALA", "GUINEA", 
    "GUINEA BISSAU", "GUYANA", "HAITI", "HONDURAS", "HUNGARY", 
    "ICELAND", "INDIA", "INDONESIA", "IRAN", "IRAQ", 
    "IRELAND", "ISRAEL", "ITALY", "JAMAICA", "JAPAN", 
    "JORDAN", "KAZAKHSTAN", "KENYA", "KIRIBATI", "KUWAIT", 
    "KYRGYZSTAN", "LAOS", "LATVIA", "LEBANON", "LESOTHO", 
    "LIBERIA", "LIBYA", "LIECHTENSTEIN", "LITHUANIA", "LUXEMBOURG", 
    "MADAGASCAR", "MALAWI", "MALAYSIA", "MALDIVES", "MALI", 
    "MALTA", "MARSHALL ISLANDS", "MAURITANIA", "MAURITIUS", "MEXICO", 
    "MICRONESIA", "MOLDOVA", "MONACO", "MONGOLIA", "MONTENEGRO", 
    "MOROCCO", "MOZAMBIQUE", "MYANMAR", "NAMIBIA", "NAURU", 
    "NEPAL", "NETHERLANDS", "NEW ZEALAND", "NICARAGUA", "NIGER", 
    "NIGERIA", "NORTH KOREA", "NORTH MACEDONIA", "NORWAY", "OMAN", 
    "PAKISTAN", "PALAU", "PALESTINE", "PANAMA", "PAPUA NEW GUINEA", 
    "PARAGUAY", "PERU", "PHILIPPINES", "POLAND", "PORTUGAL", 
    "QATAR", "ROMANIA", "RUSSIA", "RWANDA", "SAINT KITTS AND NEVIS", 
    "SAINT LUCIA", "SAINT VINCENT AND THE GRENADINES", "SAMOA", "SAN MARINO", "SAO TOME AND PRINCIPE", 
    "SAUDI ARABIA", "SENEGAL", "SERBIA", "SEYCHELLES", "SIERRA LEONE", 
    "SINGAPORE", "SLOVAKIA", "SLOVENIA", "SOLOMON ISLANDS", "SOMALIA", 
    "SOUTH AFRICA", "SOUTH KOREA", "SOUTH SUDAN", "SPAIN", "SRI LANKA", 
    "SUDAN", "SURINAME", "SWEDEN", "SWITZERLAND", "SYRIA", 
    "TAIWAN", "TAJIKISTAN", "TANZANIA", "THAILAND", "TIMOR LESTE", 
    "TOGO", "TONGA", "TRINIDAD AND TOBAGO", "TUNISIA", "TURKEY", 
    "TURKMENISTAN", "TUVALU", "UGANDA", "UKRAINE", "UNITED ARAB EMIRATES", 
    "UNITED KINGDOM", "UNITED STATES", "URUGUAY", "UZBEKISTAN", "VANUATU", 
    "VATICAN CITY", "VENEZUELA", "VIETNAM", "YEMEN", "ZAMBIA", 
    "ZIMBABWE"
]
alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

while True:
    print("\nWelcome to Hangman!")

    country = random.choice(country_list)
    letters_in_country = []
    for letter in country:
        if letter not in letters_in_country and letter != " ":
            letters_in_country.append(letter)
    correct_guesses = []
    wrong_guesses = []
    lives = 6
    while len(letters_in_country) != 0 and lives != 0:
        print(f"\nLives left: {(lives*"•")+((6-lives)*"৹")}")
        print(stages[6-lives])
        display = ""
        for letter in country:
            if letter == " ":
                display += "  "
            elif letter in correct_guesses:
                display += letter + " "
            else:
                display += "_ "
        print(display)
        print("\nWrong guesses:", wrong_guesses)
        guess = input("Guess a letter: ").upper()
        if guess not in alphabets:
            print("\nNot an alphabet. Try again.")
        elif guess in letters_in_country:
            print("\nCorrect!")
            correct_guesses.append(guess)
            letters_in_country.remove(guess)
        elif guess in correct_guesses or guess in wrong_guesses:
            print("\nAlready guessed. Try again.")
        elif guess not in letters_in_country:
            print("\nWrong!")
            lives -= 1
            wrong_guesses.append(guess)
        else:
            print("\nERROR")
            sys.exit()
    if lives == 0:
        print(stages[6])
        print(f"\nYou Lost! The country was {country}.")
    elif len(letters_in_country) == 0:
        print(safe)
        print(f"\nVictory! You got it, the country was {country}!")
    else:
        print("ERROR")
        sys.exit()
    play_again = input("\nPlay again? (Y/N): ").upper()
    if play_again == "Y":
        continue
    elif play_again == "N":
        print("\nThanks for playing!")
        break
    else:
        print("\nInvalid input. Exiting game.")
        break