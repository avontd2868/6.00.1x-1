monthlyInterestRate      = annualInterestRate / 12
monthlyPaymentLowerBound = balance / 12
monthlyPaymentUpperBound = (balance * (1 + monthlyInterestRate) ** 12) / 12.0

previousBalance       = balance
minimumMonthlyPayment = (monthlyPaymentLowerBound + monthlyPaymentUpperBound)/ 2.0
acceptedError         = 0.01

while abs(previousBalance) >= acceptedError:
  previousBalance = balance
  for month in range(0, 12):
      previousBalance = round(((previousBalance - minimumMonthlyPayment) * (1 + monthlyInterestRate)), 2)
  if previousBalance >= 0:
      monthlyPaymentLowerBound = minimumMonthlyPayment
  else:
      monthlyPaymentUpperBound = minimumMonthlyPayment
  minimumMonthlyPayment = (monthlyPaymentLowerBound + monthlyPaymentUpperBound) / 2.0

print('Lowest Payment: ' + str(round(minimumMonthlyPayment, 2)))
