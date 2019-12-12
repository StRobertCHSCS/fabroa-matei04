#Name:		problem1.py
#Purpose:	The purpose of this program is to determine the number of heating days out of eight days that have different temperatures

#Author:	Gornic.m

#Created:	date in 12/12/2019





# get the temperatures
number_of_temps = int(input("Enter the number of temperatures: "))

# initialize total
total = 0

# compute the total number of temperatures
for i in range(number_of_temps):
    # get a temperature from the user and add to total
    temperature = float(input("Enter a temperature: "))
    total = total + temperature

# compute average based on total
average = total/number_of_temps

print("The average of the " + str(number_of_temps) + " temps is " +str(average))
print("There are 5 heating days")

   