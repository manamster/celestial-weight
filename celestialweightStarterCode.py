#Name
# Date
# Celestial Weight Program
# This program will ask the user to enter their weight and convert it to a different planet weight
# Variable List: 
# 	weight - earth weight
#	choice - user's selection from the menu
#	planet$ - the selected planet
#	newweight - the new weight depending on the user's selection 

def menu():
    """the menu of planets and input for selection and weight"""
    print("""
    1. Mercury
    2. Venus
    3. Earth
    4. Mars
    5. Jupiter
    6. Saturn
    7. Uranus
    8. Neptune""")
    choice = int(input("Which number planet do you want to convert your weight for?\n"))
    weight = int(input("What is your weight in pounds?\n"))
    return(choice, weight)

def calculation(planet, weight):
    """determines the weight depending on the selection"""
    newweight = 0
    if planet == 1:
        newweight = weight * 0.38
    elif planet == 2:
        newweight = weight * 0.91
    elif planet == 3:
        newweight = weight
    elif planet == 4:
        newweight = weight * 0.38
    elif planet == 5:
        newweight = weight * 2.34
    elif planet == 6:
        newweight = weight * 0.93
    elif planet == 7:
        newweight = weight * 0.92
    elif planet == 8:
        newweight = weight * 1.12
    else:
        print("That is not an eligable planet")
        menu()
    return newweight

def display(weight, planet, newweight):
    """displays the new weight"""
    print("Your current weight on earth is " + str(weight) + "lbs.")
    listOfPlanets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    print("The planet you chose was " + listOfPlanets[planet -1] + ".")
    print("Your new weight on " + listOfPlanets[planet -1] + " is " + str(newweight) + "lbs.")
    
def main():
    choice, weight = menu()
    newWeight = calculation(choice, weight)
    display(weight, choice, newWeight)

main()