def open_account() :
    print("new account is created.")

def deposit(balance, money):
    print("The deposit has been completed. The balance is {0} won.".format(balance+money))
    return balance+money

def withdraw(balance, money):
    if balance >= money: # 잔액이 출금보다 많으면
        print("The withdraw has been completed. The balance is {0} won.".format(balance-money))
        return balance-money
    else:
        print("The withdraw has not been completed. The balance is {0} won.".format(balance))
        return balance

def withdraw_night(balance, money): # 저녁에 출금
    commission = 100 # 수수료 100원
    return commission, balance - money - commission

balance = 0
balance = deposit(balance, 1000)
#balance = withdraw(balance,2000)
#balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 500)
print("The commission is {0} won and the balance is {1} won.".format(commission, balance))