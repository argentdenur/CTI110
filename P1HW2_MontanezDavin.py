#This program helps calculate travel budget and travel expenses
#28 Sep 2023
#CTI-110 P1HW2 - Travel Expense

print('This program calculates travel budget and expenses')

Budget = int(input('Enter Budget:'))
print(Budget)
    
Destination = (input('Input your travel destination:'))
print(Destination)

Gas = int(input('Estimated gas money spent?'))
print(Gas)

Lodging = int(input('How much money will your lodging cost?'))
print(Lodging)

Food = int(input('How much money will you spend on food?'))
print(Food)

Fun_money = int(input('How much money will you need for attractions and/or souvenirs?'))
print(Fun_money)

Emergency_fund = int(input('Emergency fund:'))
print(Emergency_fund)

Total_expenses = (Gas + Lodging + Food + Fun_money + Emergency_fund)

print('---------------')

print('Location:', Destination)
print('Initial budget:', Budget)

print('Gas:', Gas)
print('Lodging:', Lodging)
print('Food:', Food)
print('Fun money:', Fun_money)
print('Emergency fund:', Emergency_fund)

print('Total expenses:', Total_expenses)
print('Remaining balance:', Budget - Total_expenses)


