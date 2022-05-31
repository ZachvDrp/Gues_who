#Choose a random character
import random

Choose_Character = random.choice(["Alex", "Alfred", "Anita", "Anne"])

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
elif Choose_Character == "Alfred":
    Gender = "Men"
    Hair_Color = "Red"
    Hair_Length = "Long"
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
elif Choose_Character == "Anne":
    Gender = "Women"
    Hair_Color = "Black"
    Hair_Length = "Short"
    Nose_Size = "Big"
    Facial_Hair = "No"
    Jewellery = "Earrings"
    Wears_Hat = "No"

#Loop questions
Character_Guess = ""

while Character_Guess != Choose_Character:
    #Questions
    Question = input("What question would you like to ask? ").lower()
    if Question == "is it a men?" or Question == "is it a men":
        if Gender == "Men":
            print("Yes")
        else:
            print("No")
    elif Question == "is the hair color blond?" or Question == "is the hair color blond":
        if Hair_Color == "Blond":
            print("Yes")
        else:
            print("No")
    elif Question == "is it Alex?" or Question == "is it Alex":
        if Choose_Character == "Alex":
            Character_Guess = "Alex"
            print("Yes, you won the game.")
        else:
            print("No, try again")
    elif Question == "is it Alfred?" or Question == "is it Alfred":
        if Choose_Character == "Alfred":
            Character_Guess = "Alfred"
            print("Yes, you won the game.")
            #exit()
        else:
            print("No, try again")
    elif Question == "is it Anita?" or Question == "is it Anita":
        if Choose_Character == "Anita":
            Character_Guess = "Anita"
            print("Yes, you won the game.")
            #exit()
        else:
            print("No, try again")
    elif Question == "is it Anne?" or Question == "is it Anne":
        if Choose_Character == "Anne":
            Character_Guess = "Anne"
            print("Yes, you won the game.")
            #exit()
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
