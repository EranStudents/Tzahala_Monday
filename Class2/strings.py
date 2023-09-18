'''
לכל תו בתוך משתנה מסוג מחרוזת
יש מיקום, המיקום מתחיל מ-0
והמיקום האחרון הוא אורך המחרוזת פחות 1
'''

name = 'Eran Levy'
#       012345678

print(len(name))  # len - length - אורך המחרוזת, כלומר כמות התווים בה
# בשביל לגשת לתו ספיצפי בתוך מחרוזת אני ניגש אליו בדרך הבאה
# name[location]
print(name[8])

num1 = '456'
first_digit = int(num1[0])
second_digit = int(num1[1])
print(f'two first digits sum is {first_digit + second_digit}')
