from collections import deque
from typing import List


class Payment:
    def __init__(self, timestamp, acc:'Account', amount):
        self.timestamp = timestamp
        self.maturity = int(self.timestamp) + 86400000
        self.acc = acc
        self.amount = amount
        self.cashback_amount = str(int(int(self.amount) * 0.02))

    def get_status(self, timestamp) -> str:
        if int(timestamp) < self.maturity:
            return "IN_PROGRESS"
        else:
            return "CASHBACK_RECEIVED"

    def should_resolve(self, timestamp) -> bool:
        if int(timestamp) < self.maturity:  # not matured
            return False
        else:
            return True

    def add_cashback(self, timestamp ):
        self.acc.deposit(timestamp, self.cashback_amount)


class Bank:
    def __init__(self):
        self.accounts: dict[int, Account] = {}  # id: Account
        self.deposits = {}
        self.paymentID = 0
        self.payments: dict[str, Payment] = {}
        self.resolved_payments: dict[str, Payment] = {}

    def create_account(self, timestamp, accountID) -> bool:
        self.check_cashback(timestamp)
        if accountID in self.accounts:
            return False
        else:
            self.accounts[accountID] = Account(timestamp, accountID)
            return True

    def deposit(self, timestamp, accountID, amount) -> str:  # return given amount
        self.check_cashback(timestamp)
        if accountID not in self.accounts:
            return ''
        account = self.accounts[accountID]
        account.deposit(timestamp, amount)
        return str(account.get_balance())

    def transfer(self, timestamp, sourceAccountId, targetAccountId, amount) -> str:
        self.check_cashback(timestamp)
        if sourceAccountId not in self.accounts or targetAccountId not in self.accounts:
            return ''

        if sourceAccountId == targetAccountId:
            return ''
        sourceAcc = self.accounts[sourceAccountId]
        targetAcc = self.accounts[targetAccountId]

        if sourceAcc.get_balance() < int(amount):
            return ''

        sourceAcc.withdraw(timestamp, amount)
        targetAcc.deposit(timestamp, amount)

        return str(sourceAcc.get_balance())

    def top_spenders(self, timestamp, n):
        self.check_cashback(timestamp)
        accounts: List[Account] = list(self.accounts.values())
        accounts.sort(key=lambda x: (x.total_spending, -int(x.accountID[7:])), reverse=True)
        accounts = accounts[:int(n)]
        res = []
        for acc in accounts:
            res.append(f'{acc.accountID}({acc.total_spending})')

        return ','.join(res)

    def pay(self, timestamp, accountId, amount) -> str:
        self.check_cashback(timestamp)
        if accountId not in self.accounts:
            return ''
        acc = self.accounts[accountId]
        if acc.get_balance() < int(amount):
            return ''

        acc.pay(timestamp, amount)
        self.paymentID += 1
        name = f'payment{self.paymentID}'
        self.payments[name] = Payment(timestamp, acc, amount)

        return name

    def check_cashback(self, timestamp):
        to_del = [ ]
        for paymentID, payment in self.payments.items():
            if payment.should_resolve(timestamp):
                payment.add_cashback(timestamp)
                to_del.append(paymentID)
                self.resolved_payments[paymentID] = payment

        for paymentID in to_del:
            del self.payments[paymentID]
    def get_payment_status(self, timestamp, accountId, paymentID) -> str:
        self.check_cashback(timestamp)
        if accountId not in self.accounts:
            return ''
        if paymentID not in self.payments and paymentID not in self.resolved_payments:
            return ''

        if paymentID in self.payments:
            payment = self.payments[paymentID]
            if payment.acc.accountID != accountId:
                return ''
            else:
                return "IN_PROGRESS"
        else:
            payment = self.resolved_payments[paymentID]

            if payment.acc.accountID != accountId:
                return ''
            else:
                return "CASHBACK_RECEIVED"


class Account:

    def __init__(self, timestamp, accountID):
        self.timestamp = timestamp
        self.accountID = accountID
        self.balance = 0
        self.total_spending = 0
        self.cashback = deque([])

    def __eq__(self, other: 'Account'):
        return self.accountID == other.accountID

    def __hash__(self):
        return hash(self.accountID)

    def pay(self, timestamp, amount):
        self.withdraw(timestamp, amount)

    def deposit(self, timestamp, amount: str):
        self.balance += int(amount)
        return

    def get_balance(self):
        return self.balance

    def add_to_total_spending(self, amount):
        self.total_spending += int(amount)

    def withdraw(self, timestamp, amount):
        self.balance -= int(amount)
        self.add_to_total_spending(amount)
        if self.balance < 0:
            print('Error in transer')
            return False
        return True


if __name__ == '__main__':
    bank = Bank()
    MILLISECONDS_IN_1_DAY = 86400000
    arr = [["CREATE_ACCOUNT", "1", "account1"],
           ["CREATE_ACCOUNT", "2", "account2"],
           ["DEPOSIT", "3", "account1", "2000"],
           ["PAY", "4", "account1", "1000"],
           ["PAY", "100", "account1", "1000"],
           ["GET_PAYMENT_STATUS", "101", "nonexisting", "payment1"],
           ["GET_PAYMENT_STATUS", "102", "account2", "payment1"],
           ["TOP_SPENDERS", "104", "2"],
           ["DEPOSIT", str(3 +
                           MILLISECONDS_IN_1_DAY), "account1",
            "100"],

           ["GET_PAYMENT_STATUS", str(4 +
                                      MILLISECONDS_IN_1_DAY), "account1",
            "payment1"],

           ["DEPOSIT", str(5 +
                           MILLISECONDS_IN_1_DAY), "account1",
            "100"],

           ["DEPOSIT", str(99 +
                           MILLISECONDS_IN_1_DAY), "account1",
            "100"],

           ["DEPOSIT", str(100 +
                           MILLISECONDS_IN_1_DAY), "account1",
            "100"]]

    for instruction in arr:
        # bank.check_cashback()
        if instruction[0] == 'CREATE_ACCOUNT':
            print(bank.create_account(*instruction[1:]))
        elif instruction[0] == 'DEPOSIT':
            print(bank.deposit(*instruction[1:]))
        elif instruction[0] == 'TRANSFER':
            print(bank.transfer(*instruction[1:]))
        elif instruction[0] == 'TOP_SPENDERS':
            print(bank.top_spenders(*instruction[1:]))
        elif instruction[0] == 'PAY':
            print(bank.pay(*instruction[1:]))
        elif instruction[0] == 'GET_PAYMENT_STATUS':
            print(bank.get_payment_status(*instruction[1:]))