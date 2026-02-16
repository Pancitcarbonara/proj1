"""
Code by KURT ASLAN ROMERO FROM 1st YEAR BSCS-DS
"""

bike = int(input('Enter the cost of the bike: '))
if (bike > 100000):
    tax = bike * 0.15
    print('Your tax is  15%, the total is:', tax)
elif (bike >50000):
    tax = bike * 0.10
    print('Your tax is  10% the total is:', tax)
else:
    tax = bike * 0.05
    print('Your tax is  5% the total is:', tax)
