# Author:           Eden Boychyn, 100752815
# Date:             February 1st, 2021
# Description       An application that takes a user's input of pizza   
#                   in inches and displays the original diameter of pizza, 
#                   number of slices it yields, and the area of each slice 
#                   using Area formulas, compound conditions, try and except
#                   statements and if, elif, else statements

# Declare and Initialize Variables
pizza_diameter = ("")
slices_of_pizza = int(pizza_diameter)
area_of_pizza = int((pizza_diameter/2)**2)*X
area_of_slice_of_pizza = int((pizza_diameter/2)**2)*X / slices_of_pizza



# Declare and initalize Constants  
import math

X = math.pi

MIN_PIZZA_DIAMETER = 8
MAX_PIZZA_DIAMETER = 24

MIN_EXTRA_SMALL = 8
MAX_EXTRA_SMALL = 11.99

MIN_SMALL = 12
MAX_SMALL = 13.99

MIN_MEDIUM = 14
MAX_MEDIUM = 15.99

MIN_LARGE = 16
MAX_LARGE = 19.99

MIN_EXTRA_LARGE = 20
MAX_EXTRA_LARGE = 24

# Prompt the user to enter the Diameter of the Pizza in inches
pizza_diameter = input("Please enter the diameter of your pizza in inches : ")

# Ensure that the user input is numeric using “try … except”
try: pizza_diameter.isnumeric():
    pizza_diameter = int(input("Please enter the diameter of your pizza in inches : ")
    #If PizzaDiameter is not a numeric value, set it to an invalid value 
except: 
    #Display error message indicating that input needs to be numeric
    print("ENTRY ERROR: Pizza must have a diameter in the range of 8 inches to 24 inches inclusive! Please try again.")

    if pizza_diameter < MIN_PIZZA_DIAMETER
        #Display message indicating that the pizza diameter in inches must be above or equal to 8"
        print("ENTRY ERROR: Pizza must have a diameter in the range of 8 inches to 24 inches inclusive!") 
        input("\nPress enter key to exit...")

    elif pizza_diameter > MAX_PIZZA_DIAMETER
        #Display message indicating that the pizza diameter in inches must be below or equal to 24"
        print("ENTRY ERROR: Pizza must have a diameter in the range of 8 inches to 24 inches inclusive!") 
        input("\nPress enter key to exit...")

    else pizza_diameter>= MIN_PIZZA_DIAMETER and <= MAX_PIZZA_DIAMETER
        # So if the pizza diameter is less than the MAX_PIZZA DIAMETER and more than the 
        # MIN_PIZZA_DIAMETER, it is assumed that the pizza diameter is within range

            # Determine the number of slices to cut the pizza in by using if/else statements
        if pizza_diameter>= MIN_EXTRA_SMALL and <= MAX_EXTRA_SMALL
            slices_of_pizza == pizza_diameter>= MIN_SMALL and <= MAX_SMALL
            print("The number of slices to cut the pizza into is: " + slices_of_pizza)

            # If pizza_diameter>= MIN_SMALL and <= MAX_SMALL determine the number of slices in a small pizza
        elif pizza_diameter>= MIN_SMALL and <= MAX_SMALL
            slices_of_pizza == pizza_diameter>= MIN_SMALL and <= MAX_SMALL
            print("The number of slices to cut the pizza into is: " + slices_of_pizza)
        
            #If pizza_diameter>= MIN_MEDIUM and MAX_MEDIUM, determine the number of slices in a medium pizza
        elif pizza_diameter>= MIN_MEDIUM and <= MAX_MEDIUM
            slices_of_pizza == pizza_diameter>= MIN_MEDIUM and <= MAX_MEDIUM
            print("The number of slices to cut the pizza into is: " + slices_of_pizza) 
        
            #If pizza_diameter>= MIN_LARGE and MAX_LARGE, determine the number of slices in a medium pizza
        elif pizza_diameter>= MIN_LARGE and <= MAX_LARGE
            slices_of_pizza == pizza_diameter>= MIN_LARGE and <= MAX_LARGE
            area_of_pizza = int((pizza_diameter/2)**2)*X
            print("The number of slices to cut the pizza into is: " + slices_of_pizza) 
        
            #If pizza_diameter>= MIN_EXTRA_LARGE and MAX_EXTRA_LARGE, determine the number of slices in a medium pizza
        else pizza_diameter>= MIN_EXTRA_LARGE and MAX_EXTRA_LARGE
            slices_of_pizza == pizza_diameter>= MIN_EXTRA_LARGE and MAX_EXTRA_LARGE
            print("The number of slices to cut the pizza into is: " + slices_of_pizza)

# Calculate the area of each pizza
area_of_pizza = int((pizza_diameter/2)**2)*X

# Calculate the area of each slice of the pizza
area_of_slice_of_pizza = int((pizza_diameter/2)**2)*X / slices_of_pizza

# Display the final result as a concatenated string message including the original pizza diameter in inches,
# the number of slices, as well as the area of each slice as a real number rounded to two decimal places
print("\n"" A pizza with a diameter of " + int(pizza_diameter) + " will yield " + int(slices_of_pizza) ". Each slice will have an area of " + float(round(area_of_slice_of_pizza,2)) " square inches.")

#Prompt the user to end the application
input("\nPress enter key to end application...")










