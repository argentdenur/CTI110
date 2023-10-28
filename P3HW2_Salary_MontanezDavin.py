#CTI-110
#P3HW2 - Salary
#Davin Montanez
#25 OCT 2023
#

#This program records hours worked, pay rate, and calculates total payment

#asks for the employee name

employee_name = (input('Enter employee name:'))

#asks employee for number of hours worked

hours_worked = float(input('Enter hours worked this week:'))

#asks employee for pay rate

pay_rate = float(input('Enter employee pay rate:'))

print('-----------------------------')

#display employee name

print('Employee name:', employee_name, '\n')

#calculate any overtime pay 

if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
else:
    overtime_hours = 0
    overtime_pay = 0

#calculate regular pay

regular_pay = (hours_worked - overtime_hours) * pay_rate

#calculate gross pay

gross_pay = regular_pay + overtime_pay

#display results of user inputs and calculations

print('Hours worked   Pay Rate   OverTime   OverTime Pay   RegHour Pay   Gross Pay')

print('----------------------------------------------------------------------------')
    
print(f'{hours_worked:<15.2f}{pay_rate:<11.1f}{overtime_hours:<7.2f}{overtime_pay:10.2f}{regular_pay:15.2f}{gross_pay:14.2f}')
