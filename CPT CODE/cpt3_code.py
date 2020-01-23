'''
-------------------------------------------------------------------------------
#Name:		cpt3_code.py
#Purpose:    determines the number of calories burnt depending on steps taken
#Author:	Gornic.M and Harold.P

#Created:	date in 23/01/2020
------------------------------------------------------------------------------
'''


#initialize counters
number_meals = 0
total_consumed = 0
steps_taken = 0

# loop to get user daily amounts and accumulate total
while steps_taken!= -1:
    steps_taken = float(input("Enter a daily setps taken amount (-1 to stop): "))
    total_consumed = total_consumed + steps_taken
    number_meals = total_consumed + 1

# compute allowable spent
allowable_consumed = total_consumed * 0.04

print("Total amount of steps: " + str(total_consumed))

print("Total amount of calores burnt: " + str(allowable_consumed))
