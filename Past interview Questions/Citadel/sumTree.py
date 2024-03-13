# Given an array, get the difference between each number by O(n)
# Modify the array and get difference in O(1)


# Design a class with 3 functionalities
# Init with an array of length n
# Get Average with runtime strictly less than O(n)
# Modify the array's entry with run time strictly less than O(n)
# The get can modify operation interleave

class SumTree:
    def __init__(self, sum, i, j, m):
        self.sum = sum
        self.i = i
        self.j = j
        self.m = m
        self.parent = None
        self.left = None
        self.right = None

    def getSum(self, i, j):
        if i <= self.i and j >= self.j:  # root totally in the interval
            return self.sum
        if self.j <= i or self.i >= j:  # root totally misses the interval
            return 0
        curr_sum = 0
        if i <= self.m and self.left is not None:  # If start of interval is prior to end of the previous one
            curr_sum += self.left.getSum(i, j)
        if j > i and self.right is not None:
            curr_sum += self.right.getSum(i, j)
        return curr_sum

    def findNode(self, i, j):
        if self.i == i and self.j == j:
            return self
        if self.i <= i and self.m >= j and self.left != None:
            return self.left.findNode(i, j)
        if self.m <= i and self.j >= j and self.right != None:
            return self.right.findNode(i, j)


class AverageList:
    def __init__(self, nums):
        prefix_sum = [0]
        curr = 0
        for num in nums:
            curr += num
            prefix_sum.append(curr)
        print(prefix_sum)
        self.sum_tree = self.buildTree(prefix_sum, 0, len(nums))

    def buildTree(self, prefix_sum, i, j):
        if i == j - 1:
            return SumTree(prefix_sum[j] - prefix_sum[i], i, j, i)
        m = (i + j) // 2
        root = SumTree(prefix_sum[j] - prefix_sum[i], i, j, m)
        root.left = self.buildTree(prefix_sum, i, m)
        root.right = self.buildTree(prefix_sum, m, j)
        if root.left != None:
            root.left.parent = root
        if root.right != None:
            root.right.parent = root
        return root

    def getAverage(self, i, j):
        return self.sum_tree.getSum(i, j) / (j - i)

    def modifyVal(self, i, new_val):
        node = self.sum_tree.findNode(i, i + 1)
        delta = new_val - node.sum
        curr = node
        print(node.sum, node.i, node.j)
        while curr != None:
            curr.sum += delta
            curr = curr.parent


avg_list = AverageList([1, 3, 5, 7, 9])
print(avg_list.getAverage(0, 3))  # 3
print(avg_list.getAverage(0, 5))  # 5
print(avg_list.getAverage(2, 5))  # 7
avg_list.modifyVal(2, 11)
print(avg_list.getAverage(0, 3))  # 5
print(avg_list.getAverage(0, 5))  # 6.2
print(avg_list.getAverage(2, 5))  # 9



