monthlyInterestRate   = annualInterestRate / 12
minimumMonthlyPayment = 0
previoustBalance      = balance
while previoustBalance > 0:
  minimumMonthlyPayment += 10
  previoustBalance      = balance
  for i in range(1, 13):
    monthlyUnpaidBalance = previoustBalance - minimumMonthlyPayment
    previoustBalance     = monthlyUnpaidBalance * (1 + monthlyInterestRate)

print ('Lowest Payment: ' + str(minimumMonthlyPayment))
