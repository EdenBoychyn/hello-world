# Author:           Eden Boychyn, 100752815
# Date:             February 1st, 2021
# Description       An application that takes a user's input of pizza   
#                   in inches and displays the original diameter of pizza, 
#                   number of slices it yields, and the area of each slice 
#                   using Area formulas, compound conditions, try and except
#                   statements and if, elif, else statements

# Import the math class 
import math

# Declare and initalize Constants  
PI = math.pi 

MIN_PIZZA_DIAMETER = 8
MAX_PIZZA_DIAMETER = 24

MIN_EXTRA_SMALL = 8
MAX_EXTRA_SMALL = 12

MIN_SMALL = 12
MAX_SMALL = 14

MIN_MEDIUM = 14
MAX_MEDIUM = 16

MIN_LARGE = 16
MAX_LARGE = 20

MIN_EXTRA_LARGE = 20
MAX_EXTRA_LARGE = 24

SIX_SLICES = 6
EIGHT_SLICES = 8
TEN_SLICES = 10
TWELVE_SLICES = 12
SIXTEEN_SLICES = 16

# Declare and Initialize Variables
pizza_diameter = 0.0
#slices_of_pizza = int(pizza_diameter)
slices_of_pizza = 0
#area_of_pizza = int((pizza_diameter/2)**2)*X
area_of_pizza = 0.0
#area_of_slice_of_pizza = int((pizza_diameter/2)**2)*X / slices_of_pizza
area_of_slice_of_pizza = 0.0


# Prompt the user to enter the Diameter of the Pizza in inches
# Ensure that the user input is numeric using “try … except”
try:
    pizza_diameter = float(input("Please enter the diameter of your pizza in inches : "))
    # If pizza__diameter is not a numeric value, set it to an invalid value 
except: 
    # Display error message indicating that input needs to be numeric
    print("ENTRY ERROR: Pizza must have a diameter in the range of 8 inches to 24 inches inclusive! Please try again.")

else: # check input is in the range of 8 to 24 inches in diameter

    if pizza_diameter >= MIN_PIZZA_DIAMETER and pizza_diameter <= MAX_PIZZA_DIAMETER:
        

        # MIN_PIZZA_DIAMETER, it is assumed that the pizza diameter is within range

            # Determine the number of slices to cut the pizza in by using if/else statements
        if pizza_diameter>= MIN_EXTRA_SMALL and pizza_diameter < MAX_EXTRA_SMALL:
            # slices_of_pizza == pizza_diameter>= MIN_SMALL and < MAX_SMALL
            slices_of_pizza = SIX_SLICES
            print("The number of slices to cut the pizza into is: " + str(slices_of_pizza))

        elif pizza_diameter>= MIN_SMALL and pizza_diameter <= MAX_SMALL:
            # slices_of_pizza == pizza_diameter>= MIN_SMALL and <= MAX_SMALL
            slices_of_pizza = EIGHT_SLICES
            print("The number of slices to cut the pizza into is: " + str(slices_of_pizza))
        
        elif pizza_diameter>= MIN_MEDIUM and pizza_diameter < MAX_MEDIUM:
            # slices_of_pizza == pizza_diameter>= MIN_MEDIUM and <= MAX_MEDIUM
            slices_of_pizza = TEN_SLICES
            print("The number of slices to cut the pizza into is: " + str(slices_of_pizza)) 
        
        elif pizza_diameter>= MIN_LARGE and pizza_diameter <= MAX_LARGE:
            slices_of_pizza = TWELVE_SLICES
            print("The number of slices to cut the pizza into is: " + str(slices_of_pizza)) 
        
        else:
            # slices_of_pizza == pizza_diameter>= MIN_EXTRA_LARGE and MAX_EXTRA_LARGE
            slices_of_pizza = SIXTEEN_SLICES
            print("The number of slices to cut the pizza into is: " + str(slices_of_pizza))
        
        # Calculate the area of each pizza
        area_of_pizza = PI * ((pizza_diameter/2)**2)

        # Calculate the area of each slice of the pizza
        area_of_slice_of_pizza = area_of_pizza / slices_of_pizza

        # Display the final result as a concatenated string message including the original pizza diameter in inches,
        # the number of slices, as well as the area of each slice as a real number rounded to two decimal places
        print("A pizza with a diameter of " + str(pizza_diameter) + " will yield " + str(slices_of_pizza) + ". Each slice will have an area of " + str(round(area_of_slice_of_pizza,2)) + " square inches.")


    else: # Else input is outside of diameter range, display error message
        # Display message indicating that the pizza diameter in inches must be above or equal to 8"
        print("ENTRY ERROR: Pizza must have a diameter in the range of 8 inches to 24 inches inclusive!")

# Prompt the user to end the application
input("\nPress enter key to end application...")










