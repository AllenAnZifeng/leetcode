class Bank:
    def __init__(self):
        self.accounts = {}  # accountId: account
        self.transferManager = TransferManager()

    def create_account(self, accountId):
        if accountId in self.accounts:
            return 'false'
        self.accounts[accountId] = Account(accountId)
        return 'true'

    def sort_activities(self, n):
        accs = list(self.accounts.values())
        accs.sort(key=lambda acc: [-acc.totalValue, acc.accountId])
        sorted_accs = accs[:min(n, len(accs))]
        res = []
        for acc in sorted_accs:
            res.append(f'{acc.accountId}({acc.totalValue})')
        return ', '.join(res)


class Account:
    def __init__(self, accountId, balance=0):
        self.accountId = accountId
        self.balance = 0
        self.totalValue = 0
        self.withholdAmount = 0

    def deposit(self, amount):
        self.balance += amount
        self.totalValue += amount
        return str(self.balance)

    def pay(self, amount):
        if self.balance < amount:
            return ''
        else:
            self.balance -= amount
            self.totalValue += amount
            return str(self.balance)

    def withhold(self, amount):
        self.withholdAmount += amount
        self.balance -= amount

    def reverseWithhold(self, amount):
        self.withholdAmount -= amount
        self.balance += amount

    def executeTransfer(self, amount):
        self.withholdAmount -= amount
        self.totalValue += amount


class Transfer:
    def __init__(self, id, timestamp, sourceAccount, targetAccount, amount):
        self.id = id
        self.start_ts = timestamp
        self.sourceAccount = sourceAccount
        self.targetAccount = targetAccount
        self.amount = amount
        self.expire_ts = 86400000 + timestamp  # > to expire
        self.accepted = False
        self.expired = False

    def accept_transfer(self, sourceAccount, targetAccount):
        self.accepted = True

    def expired_transfer(self):
        self.sourceAccount.reverseWithhold(self.amount)
        self.expired = True

    def accept(self):
        self.accepted = True
        self.expired = True
        self.sourceAccount.executeTransfer(self.amount)
        self.targetAccount.deposit(self.amount)


class TransferManager:
    def __init__(self):
        self.transfers:[Transfer] = []  # idx: transfer object

    def transfer(self, timestamp, sourceAccountId, targetAccountId, amount, bank):
        if sourceAccountId == targetAccountId:
            return ''
        elif sourceAccountId not in bank.accounts:
            return ''
        elif targetAccountId not in bank.accounts:
            return ''

        sourceAccount = bank.accounts[sourceAccountId]
        targetAccount = bank.accounts[targetAccountId]

        if sourceAccount.balance < amount:
            return ''

        newId = len(self.transfers)
        self.transfers.append(Transfer(newId, timestamp, sourceAccount, targetAccount, amount))
        sourceAccount.withhold(amount)
        return f'transfer{newId}'

    def check_expired(self, timestamp):
        for transfer in self.transfers[1:]:
            if not transfer.expired:
                if timestamp > transfer.expire_ts:
                    transfer.expired_transfer()

    def accept_transfer(self, timestamp, accountId, transferId, bank):
        if transferId > len(self.transfers) - 1:
            return 'false'

        transfer = self.transfers[transferId]
        if transfer.accepted:
            return 'false'
        if transfer.expired:
            return 'false'
        if timestamp > transfer.expire_ts:
            transfer.expired_transfer()
            return 'false'
        if transfer.targetAccount.accountId != accountId:
            return 'false'

        transfer.accept()
        return 'true'


def solution(queries):
    bank = Bank()

    res = []

    for q in queries:
        timestamp = int(q[1])
        if q[0] != 'ACCEPT_TRANSFER':
            bank.transferManager.check_expired(timestamp)

        # CREATE_ACCOUNT <timestamp> <accountId>
        if q[0] == 'CREATE_ACCOUNT':
            res.append(bank.create_account(q[2]))
            continue

        # DEPOSIT <timestamp> <accountId> <amount>
        elif q[0] == 'DEPOSIT':
            accountId = q[2]
            amount = int(q[3])
            if accountId not in bank.accounts:
                res.append('')
                continue
            res.append(bank.accounts[accountId].deposit(amount))
            continue

        # PAY <timestamp> <accountId> <amount>
        elif q[0] == 'PAY':
            accountId = q[2]
            amount = int(q[3])
            if accountId not in bank.accounts:
                res.append('')
                continue
            res.append(bank.accounts[accountId].pay(amount))

            # TOP_ACTIVITY <timestamp> <n>
        elif q[0] == 'TOP_ACTIVITY':
            n = int(q[2])
            res.append(bank.sort_activities(n))

        # TRANSFER <timestamp> <sourceAccountId> <targetAccountId> <amount>
        elif q[0] == 'TRANSFER':
            timestamp = int(q[1])
            sourceAccountId = q[2]
            targetAccountId = q[3]
            amount = int(q[4])
            res.append(bank.transferManager.transfer(timestamp, sourceAccountId, targetAccountId, amount, bank))

        # ACCEPT_TRANSFER <timestamp> <accountId> <transferId>
        elif q[0] == 'ACCEPT_TRANSFER':
            timestamp = int(q[1])
            accountId = q[2]
            if q[3][:8] != 'transfer':
                res.append('false')
                continue
            transferId = int(q[3][8:])
            res.append(bank.transferManager.accept_transfer(timestamp, accountId, transferId, bank))

        # MERGE_ACCOUNTS <timestamp> <accountId1> <accountId2>
        elif q[0] == 'MERGE_ACCOUNTS':
            timestamp = int(q[1])
            accountId1 = q[2]
            accountId2 = q[3]
            if accountId1 == accountId2:
                res.append('false')
                continue
            if accountId1 not in bank.accounts:
                res.append('false')
                continue
            if accountId2 not in bank.accounts:
                res.append('false')
                continue
            # bank.accounts.tran

    return res
