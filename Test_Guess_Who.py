#Choose a random character
import random

Choose_Character = random.choice(["Alex", "Anita"])

#Set variables for the characteristics

Gender = ""
Hair_Color = ""
Hair_Length = ""
Nose_Size = ""
Facial_Hair = ""
Jewellery = ""
Wears_Hat = ""

if Choose_Character == "Alex":
    Gender = "Men"
    Hair_Color = "Black"
    Hair_Length = "Short"
    Nose_Size = "Small"
    Facial_Hair = "Mustache"
    Jewellery = "No"
    Wears_Hat = "No"
elif Choose_Character == "Anita":
    Gender = "Women"
    Hair_Color = "Blond"
    Hair_Length = "Long"
    Nose_Size = "Small"
    Facial_Hair = "No"
    Jewellery = "No"
    Wears_Hat = "No"

#Loop questions
Character_Guess = ""

while Character_Guess != Choose_Character:
    #Questions
    Question = input("What question would you like to ask? \n").lower()
    if Question == "is it a men?" or Question == "is it a men":
        if Gender == "Men":
            print("Yes")
        else:
            print("No")
    elif Question == "is it a women?" or Question == "is it a women":
        if Gender == "Women":
            print("Yes")
        else:
            print("No")
    elif Question == "is the hair color blond?" or Question == "is the hair color blond":
        if Hair_Color == "Blond":
            print("Yes")
        else:
            print("No")
    elif Question == "is the hair color black?" or Question == "is the hair color black":
        if Hair_Color == "Black":
            print("Yes")
        else:
            print("No")
    elif Question == "is it alex?" or Question == "is it alex":
        if Choose_Character == "Alex":
            print("Yes, you won the game. \nCongratulations")
            Character_Guess = Choose_Character
        else:
            print("No, try again")
    elif Question == "is it anita?" or Question == "is it anita":
        if Choose_Character == "Anita":
            print("Yes, you won the game. \nCongratulations")
            Character_Guess = Choose_Character
        else:
            print("No, try again")


#print(Choose_Character)
#print(Gender)
#print(Hair_Color)
#print(Hair_Length)
#print(Nose_Size)
#print(Facial_Hair)
#print(Jewellery)
#print(Wears_Hat)
