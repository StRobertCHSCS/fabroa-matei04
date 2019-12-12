#Name:		problemo2.py
#Purpose:	The purpose of this program is to determine how many calories a person is consuming a day relevant to their budget of 2000

#Author:	Gornic.m

#Created:	date in 12/12/2019




#initialize counters
number_meals = 0
total_consumed = 0
daily_amount = 0

# loop to get user daily amounts and accumulate total
while daily_amount != -1:
    daily_amount = float(input("Enter a daily spent amount (-1 to stop): "))
    total_consumed = total_consumed + daily_amount
    number_meals = total_consumed + 1

# compute allowable spent
allowable_consumed = number_meals * 2000

print("Total meals eaten: " +str(number_meals))
print("Total amount consumed: " + str(total_consumed))

if total_consumed > allowable_consumed:
    fee = total_consumed * 1
    print("You consumed too many calories by: calaroies" +str(round(fee,2)))
else:
    print("Phew, you did not consume too many calories")