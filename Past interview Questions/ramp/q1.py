from typing import Dict


class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.total_value_of_transactions = 0

    def deposit(self, amount):
        self.balance += amount
        self.total_value_of_transactions += amount

    def withdraw(self, amount):
        if self.balance < amount:
            raise Exception("Insufficient balance")
        self.balance -= amount
        self.total_value_of_transactions += amount

    def __str__(self):
        return f"{self.name}: {self.balance}"


class Bank:
    def __init__(self):
        self.accounts: Dict[str, Account] = {}
        self.transfers: Dict[int, Transfer] = {}
        self.transferID = 1
        self.MILLISECONDS_IN_1_DAY = 86400000

    def check_expiration(self,time):
        for k,v in self.transfers:
            if v.time + self.MILLISECONDS_IN_1_DAY <= time:
                self.accounts[v.source]
                del self.transfers[k]

    def create_account(self,time, account_id):
        self.check_expiration(time)
        if account_id in self.accounts:
            return "false"
        self.accounts[account_id] = Account(account_id, 0)
        return "true"

    def deposit(self,time, account_id, amount):
        amount = int(amount)
        if account_id not in self.accounts:
            return ""
        self.accounts[account_id].deposit(amount)
        return str(self.accounts[account_id].balance)

    def pay(self,time, account_id, amount):
        amount = int(amount)
        if account_id not in self.accounts:
            return ""
        try:
            self.accounts[account_id].withdraw(amount)
        except Exception:
            return ""
        return str(self.accounts[account_id].balance)

    def top_activity(self,time, n: int):
        sorted_accounts = sorted(self.accounts.values(),
                                 key=lambda x: (-x.total_value_of_transactions, x.name),
                                 reverse=False)
        return ", ".join([f"{account.name}({account.total_value_of_transactions})" for account in sorted_accounts[:n]])

    def create_transfer(self,time,source,target,amount):
        if source not in self.accounts.keys() or target not in self.accounts.keys():
            return ''
        if self.accounts[source].balance < amount:
            return ''

        self.transfers[self.transferID] = Transfer(time,source,target,amount)
        self.accounts[source].balance -= amount
        self.transferID += 1
        return f'transfer{self.transferID-1}'

    def accept_transfer(self,time,account,transferID):
        if transferID not in self.transfers:
            return 'false'

        self.accounts[account] += self.transfers[transferID].amount
        return 'true'

class Transfer:
    def __init__(self,time,source,target,amount):
        self.time = time
        self.source = source
        self.target = target
        self.amount = amount




def solution(queries):
    bank = Bank()
    res = []
    for query in queries:
        if query[0] == "CREATE_ACCOUNT":
            res.append(bank.create_account(int(query[1]),query[2]))
        elif query[0] == "DEPOSIT":
            res.append(bank.deposit(int(query[1]),query[2], query[3]))
        elif query[0] == "PAY":
            res.append(bank.pay(int(query[1]),query[2], query[3]))
        elif query[0] == "TOP_ACTIVITY":
            res.append(bank.top_activity(int(query[1]),int(query[2])))
        elif query[0] == 'TRANSFER':
            res.append(bank.create_transfer(int(query[1]),query[2],query[3],int(query[4])))
        elif query[0] == 'ACCEPT_TRANSFER':
            res.append(bank.accept_transfer(int(query[1]), query[2], query[3]))

    return res