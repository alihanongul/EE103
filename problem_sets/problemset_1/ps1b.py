
yearly_salary = float(input("Enter your starting yearly salary: "))
portion_saved = float(input("Ener the percentage of your salary to save: ")) / 100
cost_of_dream_home = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter your semi-annual raise percentage: ")) / 100


portion_down_payment = 0.25
down_payment = cost_of_dream_home * portion_down_payment
amount_saved = 0
r = 0.05
months = 0


while (amount_saved < down_payment):
    months += 1
    monthly_interest = amount_saved * (r / 12)
    amount_saved += (((yearly_salary / 12) * portion_saved) + monthly_interest)
    if (months % 6 == 0):
        yearly_salary += yearly_salary * semi_annual_raise

print(f"Number of months: {months}")

