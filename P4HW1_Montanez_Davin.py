#CTI-110
#P2HW2 - List 2.0
#07 NOV 2023
#This program tracks input grades and calculates averages

# create an empty list to store grades
scores_total = []

# create option for user to input number of indiviual grades 
score = int(input("Enter the number of scores you would like to enter: "))
            
# create limits for grades and response for invalid input
for i in range(score):
    score = int(input(f'enter first score {i+1}: '))
    while score < 0 or score > 100:
        score = int(input('your score is invalid, please enter a value between 0 and 100:'))
    scores_total.append(score)

print('============Results============')

#display lowest score
lowest_score = min(scores_total)
print(f'Lowest Score: {lowest_score:.2f}')

#display score list after dropping lowest score
scores_total.remove(min(scores_total))
print('Adjusted List:', scores_total)

#displays average score based off user inputs
sum_scores = sum(scores_total)
average_score = sum_scores / len(scores_total)
print(f'Average Score: {average_score:.2f}')

# assign and display a letter grade to the calculated average
if 100 >= average_score >= 90:
    letter_grade = 'A'
elif 89 >= average_score >= 80:
    letter_grade = 'B'
elif 79 >= average_score >= 70:
    letter_grade = 'C'
elif 69 >= average_score >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'
print('Letter Grade:', letter_grade)
print('==============================') 
   
