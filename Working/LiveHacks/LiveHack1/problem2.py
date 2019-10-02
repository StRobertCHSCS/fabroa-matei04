Name:		problem1.py
Purpose:	determine the chicken distribution for the students in class and remainder for Mr. Fabroa

Author:	gornic.M

Created:	date in 02/10/2019

# get number of chickens and students
students = 22
chickens = float (input("Enter the number: "))

# compute distribution
mod = (students) % (chickens)
print (mod)

#output pieces and determine remainde that goes to Mr. Fabroa
print("The chicken piece distribution " + str(mod))