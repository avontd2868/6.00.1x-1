totalPaid       = 0
previousBalance = balance
for i in range(1, 13):
  print('Month: ' + str(i))
  minimumMonthlyPayment = previousBalance * monthlyPaymentRate
  totalPaid             += minimumMonthlyPayment
  previousBalance       -= minimumMonthlyPayment
  previousBalance       *= 1 + annualInterestRate / 12
  print('Minimum monthly payment: ' + str(round(minimumMonthlyPayment, 2)))
  print('Remaining balance: ' + str(round(previousBalance, 2)))

print('Total paid: ' + str(round(totalPaid, 2)))
print('Remaining balance: ' + str(round(previousBalance, 2)))
