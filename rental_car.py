import sys
'''
Section 1: Collect customer input
'''
# Prompt user to enter what type of rental they used
# The entry will be assigned to the variable rentalCode
# This particular input will be assigned as a string to the variable
rentalCode = input("(B)udget, (D)aily, or (W)eekly rental?\n")

if rentalCode == 'D' or rentalCode == 'B': #The if branch places a conditional statement according to the input of the user, if true, the following code will execute
  rentalPeriod = input("Number of Days Rented:\n")
elif rentalCode == 'W': #The code of elif branch is executed if it is true and if the previous condition is false
  rentalPeriod = input("Number of Weeks Rented:\n")

# These numerical values are assigned to the following variables
# Needed to calculate baseCharge based on rentalCode
budget_charge = 40.00
daily_charge = 60.00
weekly_charge = 190.00

# The if, elif, and else branch allows the variable baseCharge to change its value, depending on which conditional statement will result true
if rentalCode == 'B':
    baseCharge = int(rentalPeriod) * budget_charge
elif rentalCode == 'D':
    baseCharge = int(rentalPeriod) * daily_charge
else: # This code of this else branch will execute if all the previous conditional statements are false
    baseCharge = int(rentalPeriod) * weekly_charge

    
    
# Prompts user to enter the odometer readings from start to end of the rental
odoStart = input("Starting Odometer Reading:\n")
odoEnd = input("Ending Odometer Reading:\n")

# Calculates the totalMiles by taking the absolute value difference between the odometer readings
totalMiles = int(odoEnd) - int(odoStart)


## The following will calculate the charge for mileage, if there are any
if rentalCode == 'B':
  mileCharge = totalMiles * 0.25


averageDayMiles = int(totalMiles)/int(rentalPeriod)
if rentalCode == 'D':
  if averageDayMiles <= 100:
    mileCharge = 0
  elif averageDayMiles > 100:
    extraMiles = averageDayMiles - 100
    mileCharge = extraMiles * 0.25


averageWeekMiles = int(totalMiles)/int(rentalPeriod)
if rentalCode == 'W':
  if averageWeekMiles > 900:
    mileCharge = 100.00
  else:
    mileCharge = 0
  

amtDue = baseCharge + mileCharge

print('Rental Summary')
print('Rental Code: ' + rentalCode)
print('Rental Period: ' + rentalPeriod)
print('Starting Odometer: ' + odoStart)
print('Ending Odometer: ' + odoEnd)
print('Miles Driven: ' + str(totalMiles))
output = '$%.2f' % amtDue # Using '$%.2f' rounds the numerical value to 2 decimal places and adds the $ sign to the front of the numerical value
print('Amount Due: ' + output)