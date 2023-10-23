print('Welcome to the tip calculator')

bill = float(input('What was the total bill? '))
tip = int(input("Enter how much tip, 10% or 15% : "))
people = int(input("Enter the number of people :"))

total_tip = (bill * tip)/100
total_bill = total_tip + bill
bill_per_person = total_bill / people

print(f'Every person in the table needs to pay '
      f'{round(bill_per_person)}')