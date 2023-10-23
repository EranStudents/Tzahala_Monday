print('Welcome to the BMI calculator')

height = float(input("Enter your height : "))  # 1.71
weight = float(input("Enter your weight : "))

bmi = weight / (height * height)

# הפעולה round מאפשרת לנו להתייחס לכמה ספרות שנרצה אחרי הנקודה
# round(value, כמה ספרות אחרי הנקודה תרצה)
print(f'Your BMI is {round(bmi, 1)}')
