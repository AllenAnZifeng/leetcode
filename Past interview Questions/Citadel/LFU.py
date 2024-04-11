class Node:
    def __init__(self, key=-1, value=-1, prev=None, nxt=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.nxt = nxt

    def __repr__(self):
        return f'({self.key=}, {self.value=})'

class LRU:
    def __init__(self):
        self.d = {}  # key: Node
        self.least = Node()
        self.most = Node()
        self.least.nxt = self.most
        self.most.prev = self.least

    def getLength(self):
        return len(self.d)

    def remove(self, node: Node):
        prev, nxt = node.prev, node.nxt
        prev.nxt = nxt
        nxt.prev = prev

    def insert(self, node: Node):
        prev, nxt = self.most.prev, self.most
        node.prev = prev
        node.nxt = nxt
        nxt.prev = node
        prev.nxt = node

    def update(self, node: Node):
        self.remove(node)
        self.insert(node)

    def appendright(self, node: Node):
        self.d[node.key] = node
        self.insert(node)

    def delete(self, key: int):
        if key in self.d:
            node = self.d[key]
            del self.d[key]
            self.remove(node)

    def popleft(self) -> int:  # return key
        node_to_del = self.least.nxt
        self.delete(node_to_del)

        return node_to_del.key

    def __repr__(self):
        res = ''
        node = self.least.nxt
        while node != self.most:
            res+= node.__repr__() + '-->'
            node = node.nxt
        return res
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lfucount = 0
        self.key_to_val = {}  # key : val
        self.count_to_LRU = {}  # count : LRU obj
        self.key_to_count = {}  # key:count

    def __repr__(self):
        return f'{self.key_to_val=}, {self.count_to_LRU=}, {self.key_to_count=}, {self.lfucount=}'
    def getLength(self):
        return len(self.key_to_val)

    def counter(self, key):
        count = self.key_to_count[key]
        lru = self.count_to_LRU[count]

        lru.delete(key)

        self.key_to_count[key] = count + 1
        if count + 1 not in self.count_to_LRU:
            self.count_to_LRU[count + 1] = LRU()

        new_lru = self.count_to_LRU[count + 1]
        new_lru.appendright(Node(key, self.key_to_val[key]))

        if count == self.lfucount and lru.getLength() == 0:
            self.lfucount += 1

    def get(self, key: int) -> int:
        if key not in self.key_to_val:
            return -1
        self.counter(key)

        # print(self)
        return self.key_to_val[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.key_to_val and self.getLength() == self.capacity:
            # delete
            lru = self.count_to_LRU[self.lfucount]
            key_to_del = lru.popleft()
            del self.key_to_val[key_to_del]
            del self.key_to_count[key_to_del]

        if key not in self.key_to_val:
            self.key_to_val[key] = value
            self.key_to_count[key] = 0

        count = self.key_to_count[key]
        if count not in self.count_to_LRU:
            self.count_to_LRU[count] = LRU()

        # lru = self.count_to_LRU[count]
        # lru.appendright(Node(key, value))

        self.key_to_val[key] = value
        self.counter(key)
        self.lfucount = min(self.lfucount, self.key_to_count[key])
        # print(self)
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
#
# ["LFUCache","put","put","get","put","put","get"]
# [[2],[2,1],[2,2],[2],[1,1],[4,1],[2]]

obj = LFUCache(2)
print(obj.put(2, 1))
print(obj.put(2, 2))
print(obj.get(2))
print(obj.put(1, 1))
print(obj.put(4, 1))
print(obj.get(2))