mincome = int(input("Enter your monthly income: "))
mexpenses = int(input("Enter your total monthly expenses: "))

msavings = mincome - mexpenses
rate = 0.05
projected_annual_savings = (msavings * 12 + (msavings * 12 * rate))

print("Your monthly savings are $" + str(msavings) + ".")
print("Projected savings after 1 year, with savings, is $" + str(projected_annual_savings) + ".")
