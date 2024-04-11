class Database:
    def __init__(self):
        self.data = {}  # key: {field:value}

    def set(self, key, field, value):
        if key not in self.data:
            self.data[key] = {}

        d = self.data[key]
        d[field] = value

        return ''

    def get(self, key, field):
        if key not in self.data:
            return ''

        d = self.data[key]

        if field not in d:
            return ''

        return d[field]

    def delete(self, key, field):
        if key not in self.data:
            return 'false'

        d = self.data[key]

        if field not in d:
            return 'false'

        del d[field]
        return 'true'

    def scan(self, key) -> str:
        if key not in self.data:
            return ''

        d = self.data[key]
        res = []
        for field, value in d.items():
            res.append(f'{field}({value})')
        res.sort()
        return ', '.join(res)

    def scan_by_prefix(self, key, prefix):
        scan_by_key = self.scan(key)
        if scan_by_key == '':
            return ''
        res = []
        scan_by_key = scan_by_key.split(',')
        for item in scan_by_key:
            item = item.strip()
            if item.startswith(prefix):
                res.append(item)

        return ', '.join(res)


class Field:
    def __init__(self, fieldname, value, timestamp, ttl=float('inf')):
        self.fieldname = fieldname
        self.value = value
        self.timestamp = timestamp
        self.ttl = ttl

    def is_expired(self, timestamp):  # take current time stamp
        if timestamp >= self.timestamp + self.ttl:
            return True
        else:
            return False

    def __eq__(self, other: 'Field'):
        return self.fieldname == other.fieldname

    def __hash__(self):
        return hash(self.fieldname)

    def __repr__(self):
        return f'fieldname: {self.fieldname} ,value: {self.value}'


class DatabaseTTL:
    def __init__(self):
        self.data: dict[str, List[Field]] = {}
        self.backups = {}  # time: state

    def set_at(self, key, field, value, timestamp):
        if key not in self.data:
            self.data[key] = []

        arr = self.data[key]
        for f in arr:
            if f.fieldname == field:
                f.timestamp = timestamp
                f.ttl = float('inf')
                f.value = value
                return ''

        arr.append(Field(field, value, timestamp))
        return ''

    def set_at_with_ttl(self, key, field, value, timestamp, ttl):
        if key not in self.data:
            self.data[key] = []

        arr = self.data[key]
        for f in arr:
            if f.fieldname == field:
                f.timestamp = timestamp
                f.ttl = ttl
                f.value = value
                return ''

        arr.append(Field(field, value, timestamp, ttl))
        return ''

    def get_at(self, key, field, timestamp):
        if key not in self.data:
            return ''

        arr = self.data[key]

        for f in arr:
            if f.fieldname == field and f.is_expired(timestamp) == False:
                return f.value

        return ''

    def delete_at(self, key, field, timestamp):
        if key not in self.data:
            return 'false'

        arr = self.data[key]

        for f in arr:
            if f.fieldname == field and f.is_expired(timestamp) == False:
                arr.remove(f)
                return 'true'

        return 'false'

    def scan_at(self, key, timestamp) -> str:
        if key not in self.data:
            return ''

        arr = self.data[key]
        res = []
        for f in arr:
            print(f.is_expired(timestamp))
            if f.is_expired(timestamp) == False:
                field = f.fieldname
                value = f.value
                res.append(f'{field}({value})')
        res.sort()
        print('res', res, 'arr', arr, 'time', timestamp)

        return ', '.join(res)

    def scan_by_prefix_at(self, key, prefix, timestamp):
        scan_by_key = self.scan_at(key, timestamp)
        if scan_by_key == '':
            return ''
        res = []
        scan_by_key = scan_by_key.split(',')
        for item in scan_by_key:
            item = item.strip()
            if item.startswith(prefix):
                res.append(item)

        return ', '.join(res)

    def backup(timestamp):
        pass

    def restore(timestamp, timestampToRestore):
        pass


def solution(queries):
    db = Database()
    db_time = DatabaseTTL()

    res = []

    for querry in queries:
        if querry[0] == 'SET':
            res.append(db.set(querry[1], querry[2], querry[3]))
        elif querry[0] == 'GET':
            res.append(db.get(querry[1], querry[2]))
        elif querry[0] == 'DELETE':
            res.append(db.delete(querry[1], querry[2]))
        elif querry[0] == 'SCAN':
            res.append(db.scan(querry[1]))
        elif querry[0] == 'SCAN_BY_PREFIX':
            res.append(db.scan_by_prefix(querry[1], querry[2]))


        elif querry[0] == 'SET_AT':
            res.append(db_time.set_at(querry[1], querry[2], querry[3], int(querry[4])))
        elif querry[0] == 'SET_AT_WITH_TTL':
            res.append(db_time.set_at_with_ttl(querry[1], querry[2], querry[3], int(querry[4]), int(querry[5])))
        elif querry[0] == 'DELETE_AT':
            res.append(db_time.delete_at(querry[1], querry[2], int(querry[3])))
        elif querry[0] == 'GET_AT':
            res.append(db_time.get_at(querry[1], querry[2], int(querry[3])))
        elif querry[0] == 'SCAN_AT':
            res.append(db_time.scan_at(querry[1], int(querry[2])))
        elif querry[0] == 'SCAN_BY_PREFIX_AT':
            res.append(db_time.scan_by_prefix_at(querry[1], querry[2], int(querry[3])))
        elif querry[0] == 'BACKUP':
            res.append(db_time.backup(querry[1], int(querry[2])))
        elif querry[0] == 'RESTORE':
            res.append(db_time.restore(querry[1], int(querry[2]), int(querry[3])))

    return res
