from typing import List


class Bank:
    def __init__(self):
        self.accounts: dict[int, Account] = {}  # id: Account
        self.deposits = {}

    def create_account(self, timestamp, accountID) -> bool:
        if accountID in self.accounts:
            return False
        else:
            self.accounts[accountID] = Account(timestamp, accountID)
            return True

    def deposit(self, timestamp, accountID, amount) -> str:  # return given amount
        if accountID not in self.accounts:
            return ''
        account = self.accounts[accountID]
        account.deposit(amount)
        return amount

    def transfer(self, timestamp, sourceAccountId, targetAccountId, amount) -> str:
        if sourceAccountId not in self.accounts or targetAccountId not in self.accounts:
            return ''

        if sourceAccountId == targetAccountId:
            return ''
        sourceAcc = self.accounts[sourceAccountId]
        targetAcc = self.accounts[targetAccountId]

        if sourceAcc.get_balance() < int(amount):
            return ''

        sourceAcc.transfer(amount)
        targetAcc.deposit(amount)

        return str(sourceAcc.get_balance())

    def top_spenders(self, timestamp, n):
        accounts: List[Account] = list(self.accounts.values())
        accounts.sort(key=lambda x: (-x.total_spending, x.accountID))
        accounts = accounts[:int(n)]
        res = []
        for acc in accounts:
            res.append(f'{acc.accountID}({acc.total_spending})')

        return ','.join(res)


class Account:

    def __init__(self, timestamp, accountID):
        self.timestamp = timestamp
        self.accountID = accountID
        self.balance = 0
        self.total_spending = 0

    def __eq__(self, other: 'Account'):
        return self.accountID == other.accountID

    def __hash__(self):
        return hash(self.accountID)

    def deposit(self, amount: str):
        self.balance += int(amount)
        return

    def get_balance(self):
        return self.balance

    def add_to_total_spending(self, amount):
        self.total_spending += int(amount)

    def transfer(self, amount):
        self.balance -= int(amount)
        self.add_to_total_spending(amount)
        if self.balance < 0:
            print('Error in transer')
            return False
        return True


if __name__ == '__main__':
    bank = Bank()
    arr = [["CREATE_ACCOUNT", "1", "account3"],
           ["CREATE_ACCOUNT", "2", "account2"],
           ["CREATE_ACCOUNT", "3",
            "account1"],
           ["DEPOSIT", "4", "account1",
            "2000"],
           ["DEPOSIT", "5", "account2",
            "3000"],
           ["DEPOSIT", "6", "account3",
            "4000"],
           ["TOP_SPENDERS", "7", "3"],
           ["TRANSFER", "8", "account3",
            "account2", "500"],
           ["TRANSFER", "9", "account3",
            "account1", "1000"],
           ["TRANSFER", "10",
            "account1", "account2",
            "2500"],
           ["TOP_SPENDERS", "11", "3"]]

    for instruction in arr:
        if instruction[0] == 'CREATE_ACCOUNT':
            print(bank.create_account(*instruction[1:]))
        elif instruction[0] == 'DEPOSIT':
            print(bank.deposit(*instruction[1:]))
        elif instruction[0] == 'TRANSFER':
            print(bank.transfer(*instruction[1:]))
        elif instruction[0] == 'TOP_SPENDERS':
            print(bank.top_spenders(*instruction[1:]))
