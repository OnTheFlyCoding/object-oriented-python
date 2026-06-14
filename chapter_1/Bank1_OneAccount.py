#Non-oop
# Bank version 1.0
#Single Account

account_name = 'Gio'
account_balance = 100
account_password = 'Yankees'

while True:
    print()
    print('Press b to get balance')
    print('Press d to make a deposit')
    print('Press w to withdrawal')
    print('Print s to show account info')
    print('Press q to quit')
    print()

    action = input('What do you want to do?')
    action = action.lower()
    action = action[0]
    print()

    if action == 'b':
        print('Get Balance:')
        user_password = input('Please enter your password: ')
        if user_password != account_password:
            print('Incorrect password')
        else:
            print('Your current Balance is: ', account_balance)

    elif action =='d':
        print('Deposit Option Chosen ')
        user_password = input('Please enter your password: ')
        if user_password != account_password:
            print('Incorrect password:(')
        else:
            userDepositAmmount = input('How much would you like to deposit? \n Deposit ammount: ')
            userDepositAmmount = int(userDepositAmmount)
            if userDepositAmmount < 0 :
                print('Invalid deposit ammount!')
            else: #Ok
                account_balance += userDepositAmmount
                print('Your new updared balance is: ', account_balance)

    #Show
    elif action == 's':
        print('Showing account info...\nFetching account info...')
        print('Show:')
        print('\tName', account_name)
        print('\tBalance:', account_balance)
        print('\tPassword:', account_password)
        print()

    #Quit
    elif action == 'q':
        print('Quitting...')
        break    

    # Withdrawal 
    elif action == 'w':
        userWithdrawalAmmount = input('How much would you like to withdrawal? Withdrawal ammount: ')
        userWithdrawalAmmount = int(userWithdrawalAmmount)
        userPassword = input('Please enter your password: ')
        if userPassword != account_password:
            print('Incorrect Password!')
        elif userWithdrawalAmmount < 0 or userWithdrawalAmmount > account_balance:
                print()
                print('Invalid withdrawal ammount!')
        else: #Okay
            account_balance = account_balance - userWithdrawalAmmount
            print('Your new updated balance is: ', account_balance)

    #End
    elif action == 'q':
        print('Quitting...')
        break

print('Program end.. Goodbye.')
