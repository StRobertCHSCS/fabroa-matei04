'''
-------------------------------------------------------------------------------
#Name:		cpt_code.py
#Purpose:    determines the number of calories intook

#Author:	Gornic.M and Harold.P

#Created:	date in 23/01/2020
------------------------------------------------------------------------------
'''

#initialize counters
number_meals = 0
total_consumed = 0
daily_amount = 0

# loop to get user daily amounts and accumulate total
while daily_amount != -1:
    daily_amount = float(input("Enter a daily consumed amount (-1 to stop): "))
    total_consumed = total_consumed + daily_amount
    number_meals = total_consumed + 1

# compute allowable spent
allowable_consumed = number_meals * 4

print("Total amount consumed: " + str(total_consumed))

if total_consumed > allowable_consumed:
    fee = total_consumed * 1
    print("You consumed too many calories by: calaroies" +str(round(fee,2)))
else:
    print("Phew, you did not consume too many calories")