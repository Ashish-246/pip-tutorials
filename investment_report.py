deposit = float(input("Enter the initial deposit amount: "))
interest_rate = float(input("Enter the interest rate: "))
years = int(input("Enter the number of years to be calculated: "))

print("%-6s %-16s %-10s %-16s" % ("Year", "Opening_Balance", "Interest", "Closing_Balance"))

for year in range(1, years + 1):
    opening_balance = deposit 
    interest_amount = deposit * (interest_rate / 100)
    deposit += interest_amount
    closing_balance = deposit

    print("%-6d %-16.2f %-10.2f %-16.2f" % (year, opening_balance, interest_amount, closing_balance))