from collections import deque
from typing import List


class Payment:
    def __init__(self, timestamp, acc: 'Account', amount):
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

    def add_cashback(self, timestamp):
        self.acc.deposit(timestamp, self.cashback_amount)


class Bank:
    def __init__(self):
        self.accounts: dict[int, Account] = {}  # id: Account
        self.merged_accounts: dict[int, Account] = {}
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

    def merge_accounts(self, timestamp, accountId1, accountId2) -> bool:
        self.check_cashback(timestamp)
        if accountId1 == accountId2:
            return False
        if accountId1 not in self.accounts or accountId2 not in self.accounts:
            return False
        acc1 = self.accounts[accountId1]
        acc2 = self.accounts[accountId2]  # merge 2 to 1

        acc2.set_merge_time(timestamp)
        acc2.accountID = accountId1

        del self.accounts[accountId2]
        self.merged_accounts[accountId2] = acc2

        acc1.deposit(timestamp, str(acc2.get_balance()))
        acc1.add_to_total_spending(acc2.total_spending)

        # acc2 payment change account to acc1
        for paymentID, payment in self.payments.items():
            if payment.acc == acc2:
                payment.acc = acc1
        return True

    def get_balance(self, timestamp, accountId, timeAt):
        self.check_cashback(timestamp)

        if accountId in self.accounts:
            acc = self.accounts[accountId]
            return acc.get_balance_at_time(timeAt)

        if accountId in self.merged_accounts:
            acc = self.merged_accounts[accountId]
            # print(f'{timestamp=}, {accountId=}, {timeAt=}, {acc.merged_at_time=}')
            if timeAt < acc.timestamp: # account not created yet
                return ''
            if timeAt < acc.merged_at_time:
                return acc.get_balance_at_time(timeAt)
            else:
                return ''

        return ''

    def deposit(self, timestamp, accountID, amount) -> str:  # return given amount
        self.check_cashback(timestamp)
        if accountID not in self.accounts:
            return ''
        account = self.accounts[accountID]
        account.deposit(timestamp, amount)
        # print(account.history)
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
        to_del = []
        for paymentID, payment in self.payments.items():
            if payment.should_resolve(timestamp):
                payment.add_cashback(timestamp)
                to_del.append(paymentID)
                self.resolved_payments[paymentID] = payment

        for paymentID in to_del:
            del self.payments[paymentID]

    def get_payment_status(self, timestamp, accountId, paymentID) -> str:
        self.check_cashback(timestamp)
        # print(timestamp, accountId, paymentID)
        if accountId not in self.accounts:
            return ''
        if paymentID not in self.payments and paymentID not in self.resolved_payments:
            return ''


        if accountId in self.merged_accounts:
            accountId = self.merged_accounts[accountId].accountID

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
        # self.balance = 0
        self.total_spending = 0

        self.history = {timestamp:0}  # time: balance
        self.merged_at_time = float('inf')
        # self.merged_to_accountID = -1

    def __eq__(self, other: 'Account'):
        return self.accountID == other.accountID

    def __hash__(self):
        return hash(self.accountID)

    def set_merge_time(self, timestamp):
        self.merged_at_time = timestamp

    def pay(self, timestamp, amount):
        self.withdraw(timestamp, amount)

    def deposit(self, timestamp, amount: str):
        self.history[timestamp] = self.get_balance() + int(amount)
        return

    def get_balance(self):
        cur_time = max([int(t) for t, balance in self.history.items()])
        # print(f'get_balance {cur_time, self.history[cur_time] }')
        return self.history[str(cur_time)]

    def get_balance_at_time(self,timestamp):
        times = [int(t) for t in self.history.keys()]
        times.sort(reverse=True)
        for t in times:
            if t <= int(timestamp):
                return self.history[str(t)]

        return self.get_balance()
    def add_to_total_spending(self, amount):
        self.total_spending += int(amount)

    def withdraw(self, timestamp, amount):
        self.history[timestamp] = self.get_balance() - int(amount)
        self.add_to_total_spending(amount)
        if self.get_balance() < 0:
            print('Error in transer')
            return False
        return True


if __name__ == '__main__':
    bank = Bank()
    MILLISECONDS_IN_1_DAY = 86400000
    arr1 = [["CREATE_ACCOUNT", "1", "account1"],
            ["CREATE_ACCOUNT", "2", "account2"],
            ["DEPOSIT", "3", "account1", "2000"],
            ["DEPOSIT", "4", "account2", "2000"],
            ["PAY", "5", "account2", "300"],
            ["TRANSFER", "6", "account1",
             "account2", "500"],
            ["MERGE_ACCOUNTS", "7", "account1",
             "non-existing"],
            ["MERGE_ACCOUNTS", "8", "account1",
             "account1"],
            ["MERGE_ACCOUNTS", "9", "account1",
             "account2"],
            ["DEPOSIT", "10", "account1", "100"],
            ["DEPOSIT", "11", "account2", "100"],
            ["GET_PAYMENT_STATUS", "12",
             "account2", "payment1"],
            ["GET_PAYMENT_STATUS", "13",
             "account1", "payment1"],
            ["GET_BALANCE", "14", "account2", "1"],
            ["GET_BALANCE", "15", "account2", "9"],
            ["GET_BALANCE", "16", "account1", "11"],
            ["DEPOSIT", str(5 +
                            MILLISECONDS_IN_1_DAY), "account1",
             "100"]]



    for instruction in arr1:
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
        elif instruction[0] == 'MERGE_ACCOUNTS':
            print(bank.merge_accounts(*instruction[1:]))
        elif instruction[0] == 'GET_BALANCE':
            print(bank.get_balance(*instruction[1:]))