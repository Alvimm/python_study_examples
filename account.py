from datetime import datetime

from extract import Extract
from study.client import Client

now = datetime.now()
date_config = "%d/%m/%Y, %H:%M:%S"


class Account:
    def __init__(self, clients, number, balance):
        self.clients = clients
        self.number = number
        self.balance = balance
        self.opening_date = now.strftime(date_config)
        self.extract = Extract()

    def deposit(self, value):
        self.balance += value
        self.extract.transactions.append(['DEPOSIT', value, 'DATE', now.strftime(date_config)])

    def to_withdraw(self, value):
        if self.balance < value:
            return False
        else:
            self.balance -= value
            self.extract.transactions.append(['WITHDRAW', value, 'DATE', now.strftime(date_config)])
            return True

    def transfer_value(self, destination_account, value):
        if self.balance < value:
            return 'There is not enough balance'
        else:
            destination_account.deposit(value)
            self.balance -= value
            self.extract.transactions.append(['TRANSFER', value, 'DATE', now.strftime(date_config)])
            return 'Transfer performed'

    def generate_balance(self):
        print(f'numero: {self.number}\n saldo: {self.balance}')


client1 = Client('123', 'John', 'X street')
client2 = Client('456', 'Mary', 'Y street')
account1 = Account([client1, client2], 1, 2000)
account2 = Account(client2, 2, 10000)
account1.deposit(1000)
account1.to_withdraw(1500)
account1.extract.extracts(account1.number)
account1.transfer_value(account2, 100)
account2.extract.extracts(account2.number)
