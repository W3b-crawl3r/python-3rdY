from models import Account,CheckingAccount,SavingAccount



if __name__=='__main__':
    acc:Account = CheckingAccount(500,1000)

    acc.withdraw(500)
    acc.withdraw(300)
    acc.deposit(800)
    for c in acc.transactions:
        print(c)
    print(acc.amount)