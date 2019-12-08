
def ask_genre_or_mood():
    stop = False
    while stop == False:
        choice = input("Okay, first are you looking for music from a specific genre or to set a mood? Type genre or mood ").lower()
        if (choice == "genre"):
            stop = True
            print("\nOkay what genre are you interested in? Choose from Rap, Pop, or R&B.", end="")
        elif(choice == "mood"):
            stop = True
            print("\nOkay what mood are you trying to convey? Choose from Turnt, Sadness, or Christmas.", end="")
        else:
            stop = False
            print("\nDidn't understand that. Try again.")
            
    return choice

def ask_gender():
    stop = False
    while stop == False:
        gender = input("Okay, do you want a male or female artist? Type male or female. ").lower()
        if (gender == "male"):
            stop = True
        elif(gender == "female"):
            stop = True
        else:
            stop = False
            print("\nDidn't understand that. Try again.")
    return gender

def ask_category():
    genres = ["rap", "pop", "r&b"]
    moods = ["turnt", "sadness", "christmas"]
    
    stop = False
    while stop == False:
        category = input().lower()
        if (category in genres or category in moods):
            stop = True
        else:
            stop = False
            print("\nDidn't understand that. Try again.")
    return category