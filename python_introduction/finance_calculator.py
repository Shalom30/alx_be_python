monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses
rate = 0.05
projected_annual_savings = (monthly_savings * 12 + (monthly_savings * 12 * rate))

print("Your monthly savings are $" + str(monthly_savings) + ".")
print("Projected savings after 1 year, with savings, is $" + str(projected_annual_savings) + ".")
