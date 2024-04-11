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


class Account:

    def __init__(self, timestamp, accountID):
        self.timestamp = timestamp
        self.accountID = accountID
        self.balance = 0

    def __eq__(self, other: 'Account'):
        return self.accountID == other.accountID

    def __hash__(self):
        return hash(self.accountID)

    def deposit(self, amount: str):
        self.balance += int(amount)
        return

    def get_balance(self):
        return self.balance

    def transfer(self, amount):
        self.balance -= int(amount)
        if self.balance < 0:
            print('Error in transer')
            return False
        return True


if __name__ == '__main__':
    bank = Bank()
    arr = [["CREATE_ACCOUNT", "1", "account1"],
           ["CREATE_ACCOUNT", "2", "account1"],
           ["CREATE_ACCOUNT", "3", "account2"],
           ["DEPOSIT", "4", "non-existing", "2700"],
           ["DEPOSIT", "5", "account1", "2700"],
           ["TRANSFER", "6", "account1", "account2", "2701"],
           ["TRANSFER", "7", "account1", "account2", "200"]]

    for instruction in arr:

        if instruction[0] == 'CREATE_ACCOUNT':
            print(bank.create_account(*instruction[1:]))
        elif instruction[0] == 'DEPOSIT':
            print(bank.deposit(*instruction[1:]))
        elif  instruction[0] == 'TRANSFER':
            print(bank.transfer(*instruction[1:]))


