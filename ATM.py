import sys

account_balance = float(500.25)



def accountBalance():
  print('Your current balance:')
  print(account_balance)

#custom function that calculates the new account balance if user is depositing money in their account
def deposit(deposit_amount):
  global account_balance
  account_balance = float(account_balance) + float(deposit_amount)
  return account_balance

  
def withdrawal(withdrawal_amount): #(withdrawal_amount) is the parameter for this custom function, which is a float number
  global account_balance
  account_balance = float(account_balance) - float(withdrawal_amount)
  return account_balance #this will return the updated account balance if user chooses to withdraw from their account

userchoice = input ("What would you like to do?\n")

if (userchoice == 'B'):
  accountBalance()
elif (userchoice == 'D'):
  deposit_amount = float(input("How much would you like to deposit today?\n"))
  print('Deposit was $%.2f' % deposit_amount + ', current balance is $' + str(deposit(deposit_amount)))
elif (userchoice == 'W'):
  withdrawal_amount = float(input("How much would you like to withdraw today?\n"))
  if withdrawal_amount > account_balance:
    print('$%.2f' % withdrawal_amount + ' is greater than your account balance of $%.2f' % account_balance)
  elif withdrawal_amount < account_balance:
    print('Withdrawal amount was $%.2f' % withdrawal_amount + ', current balance is $' + str(withdrawal(withdrawal_amount)))
elif (userchoice == 'Q'):
  print('Thank you for banking with us.')