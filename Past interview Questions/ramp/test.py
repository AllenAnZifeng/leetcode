from typing import Dict


class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.total_value_of_transactions = 0
        self.balance_on_hold = 0
        self.balance_history: Dict[int, int] = {}

    def deposit(self, amount):
        self.balance += amount
        self.total_value_of_transactions += amount

    def withdraw(self, amount):
        if self.balance < amount:
            raise Exception("Insufficient balance")
        self.balance -= amount
        self.total_value_of_transactions += amount

    def hold(self, amount):
        if self.balance < amount:
            raise Exception("Insufficient balance")
        self.balance -= amount
        self.balance_on_hold += amount

    def take_away_hold(self, amount):
        if self.balance_on_hold < amount:
            raise Exception("Insufficient balance on hold")
        self.balance_on_hold -= amount
        self.total_value_of_transactions += amount

    def release_hold(self, amount):
        if self.balance_on_hold < amount:
            raise Exception("Insufficient balance on hold")
        self.balance_on_hold -= amount
        self.balance += amount

    def __str__(self):
        return f"{self.name}: {self.balance}"


class Transfer:
    def __init__(self, transfer_id: str, source_account_id: str, to_account_id: str, amount: int, timestamp: int):
        self.transfer_id = transfer_id
        self.source_account_id = source_account_id
        self.to_account_id = to_account_id
        self.amount = amount
        self.timestamp = timestamp
        self.status = "pending"

    def is_expired(self, current_timestamp: int):
        return current_timestamp - self.timestamp > 24 * 60 * 60 * 1000


class Bank:
    def __init__(self):
        self.accounts: Dict[str, Account] = {}
        self.deactivated_accounts: Dict[str, Account] = {}
        self.transfers: Dict[str, Transfer] = {}
        self.next_transfer_id = 1

    def create_account(self, account_id):
        if account_id in self.accounts:
            return "false"
        self.accounts[account_id] = Account(account_id, 0)
        return "true"

    def deposit(self, account_id, amount):
        amount = int(amount)
        if account_id not in self.accounts:
            return ""
        self.accounts[account_id].deposit(amount)
        return str(self.accounts[account_id].balance)

    def pay(self, account_id, amount):
        amount = int(amount)
        if account_id not in self.accounts:
            return ""
        try:
            self.accounts[account_id].withdraw(amount)
        except Exception:
            return ""
        return str(self.accounts[account_id].balance)

    def top_activity(self, n: int):
        sorted_accounts = sorted(self.accounts.values(),
                                 key=lambda x: (-x.total_value_of_transactions, x.name),
                                 reverse=False)
        return ", ".join([f"{account.name}({account.total_value_of_transactions})" for account in sorted_accounts[:n]])

    def transfer(self, timestamp, source_account_id, to_account_id, amount):
        if source_account_id == to_account_id:
            return ""
        if source_account_id not in self.accounts or to_account_id not in self.accounts:
            return ""
        amount = int(amount)
        if self.accounts[source_account_id].balance < amount:
            return ""

        transfer_id = f"transfer{self.next_transfer_id}"
        self.next_transfer_id += 1

        try:
            self.accounts[source_account_id].hold(amount)
        except Exception:
            return ""
        transfer = Transfer(transfer_id, source_account_id, to_account_id, amount, timestamp)
        self.transfers[transfer_id] = transfer
        return transfer_id

    def accept_transfer(self, timestamp, target_account_id, transfer_id):
        if target_account_id not in self.accounts:
            return "false"
        if transfer_id not in self.transfers:
            return "false"
        transfer = self.transfers[transfer_id]

        if transfer.to_account_id != target_account_id \
                or transfer.is_expired(timestamp) \
                or transfer.status != "pending":
            return "false"

        try:
            self.accounts[transfer.source_account_id].take_away_hold(transfer.amount)
        except Exception:
            return "false"
        self.accounts[target_account_id].deposit(transfer.amount)
        transfer.status = "accepted"
        return "true"

    def merge_accounts(self, timestamp, account_id1, account_id2):
        if account_id1 == account_id2:
            return "false"
        if account_id1 not in self.accounts or account_id2 not in self.accounts:
            return "false"

        transfers_from_2 = [t for t in self.transfers.values() if t.source_account_id == account_id2]
        for t in transfers_from_2:
            self.cancel_transfer(t)
        assert self.accounts[account_id2].balance_on_hold == 0

        transfers_from_1_to_2 = [t for t in self.transfers.values() if
                                 t.source_account_id == account_id1 and t.to_account_id == account_id2]
        for t in transfers_from_1_to_2:
            self.cancel_transfer(t)

        transfers_to_2 = [t for t in self.transfers.values() if t.to_account_id == account_id2]
        for t in transfers_to_2:
            t.to_account_id = account_id1

        self.accounts[account_id1].balance += self.accounts[account_id2].balance
        self.accounts[account_id2].balance = 0

        self.accounts[account_id1].total_value_of_transactions += self.accounts[account_id2].total_value_of_transactions

        self.deactivated_accounts[account_id2] = self.accounts[account_id2]
        del self.accounts[account_id2]

    def cancel_transfer(self, transfer):
        self.accounts[transfer.source_account_id].release_hold(transfer.amount)
        transfer.status = "cancelled"

    def cancel_expired_transfers(self, timestamp: int):
        for t in self.transfers.values():
            if t.status == "pending" and t.is_expired(timestamp):
                self.cancel_transfer(t)

    def record_balance(self, timestamp: int):
        for account in self.accounts.values():
            account.balance_history[timestamp] = account.balance

    def get_balance_at(self, timestamp: int, account_id: str, timeat:int):
        account = None
        if account_id in self.accounts:
            account = self.accounts[account_id]
        elif account_id in self.deactivated_accounts:
            account = self.deactivated_accounts[account_id]
        if timeat in account.balance_history:
            return str(account.balance_history[timeat])
        else:
            return ""

def solution(queries):
    bank = Bank()
    res = []
    for query in queries:
        timestamp = int(query[1])
        bank.cancel_expired_transfers(timestamp)

        if query[0] == "CREATE_ACCOUNT":
            res.append(bank.create_account(query[2]))
        elif query[0] == "DEPOSIT":
            res.append(bank.deposit(query[2], query[3]))
        elif query[0] == "PAY":
            res.append(bank.pay(query[2], query[3]))
        elif query[0] == "TOP_ACTIVITY":
            res.append(bank.top_activity(int(query[2])))
        elif query[0] == "TRANSFER":
            res.append(bank.transfer(timestamp, query[2], query[3], query[4]))
        elif query[0] == "ACCEPT_TRANSFER":
            res.append(bank.accept_transfer(timestamp, query[2], query[3]))
        elif query[0] == "MERGE_ACCOUNTS":
            res.append(bank.merge_accounts(timestamp, query[2], query[3]))
        bank.record_balance(timestamp)
        if query[0] == "GET_BALANCE":
            res.append(bank.get_balance_at(timestamp, query[2], int(query[3])))
    return res


if __name__ == '__main__':
    queries = [
        ["CREATE_ACCOUNT", "1", "account1"],
        ["CREATE_ACCOUNT", "2", "account2"],
        ["CREATE_ACCOUNT", "3", "account3"],
        ["DEPOSIT", "4", "account1", "2000"],
        ["DEPOSIT", "5", "account2", "2000"],
        ["DEPOSIT", "6", "account3", "2000"],
        ["TRANSFER", "7", "account1", "account3", "300"],
        ["TRANSFER", "8", "account1", "account2", "500"],
        ["TRANSFER", "9", "account2", "account3", "500"],
        ["MERGE_ACCOUNTS", "10", "account1", "account2"],
        ["PAY", "11", "account1", "1000"],
        ["PAY", "12", "account2", "10"],
        ["ACCEPT_TRANSFER", "13", "account3", "transfer1"],
        ["ACCEPT_TRANSFER", "14", "account2", "transfer2"],
        ["ACCEPT_TRANSFER", "15", "account3", "transfer3"],
        ["TOP_ACTIVITY", "16", "3"],
        ["GET_BALANCE", "17", "account2", "1"],
        ["GET_BALANCE", "18", "account2", "10"],
        ["GET_BALANCE", "19", "account1", "4"],
        ["GET_BALANCE", "20", "account1", "12"]
    ]

    print(solution(queries))
