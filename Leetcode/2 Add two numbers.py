# Definition for singly-linked list.

class ListNode:
    def __init__(self, x,next=None):
        self.val = x
        self.next = next

a=ListNode(5)
b=ListNode(2,a)
c=ListNode(0,b)

d=ListNode(4)
e=ListNode(0,d)
f=ListNode(6,e)

# from functools import reduce
# class Solution(object):
#     def get_value(self, l):  # input:linked list
#         temp = l.val
#         return temp
#
#     def get_next(self, l):
#         temp = l.next
#         return temp
#
#     def addTwoNumbers(self, l1, l2=0):
#         one = []
#         two = []
#
#         while True:
#             if self.get_next(l1) is None:
#                 one.append(l1.val)
#                 break
#             one.append(l1.val)
#             l1 = l1.next
#
#
#         while True:
#             if self.get_next(l2) is None:
#                 two.append(l2.val)
#                 break
#             two.append(l2.val)
#             l2 = l2.next
#
#
#
#         one.reverse()
#         two.reverse()
#         print("=================")
#         one = reduce(lambda x, y: x * 10 + y, one)
#         two = reduce(lambda x, y: x * 10 + y, two)
#         print(one)
#         print(two)
#         sum = one + two
#         sum = str(sum)
#
#         tmp = []
#         for digit in sum:
#             tmp.append(int(digit))
#         tmp.reverse()
#
#         print(tmp)
#         return tmp
#
#
# b=Solution()
# b.addTwoNumbers(c,f)




class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        counter=0
        num1, num2,=0,0
        while l1 is not None:
            num1+=l1.val*10**counter
            l1=l1.next
            counter+=1
        counter =0
        while l2 is not None:
            num2 += l2.val * 10 ** counter
            l2 = l2.next
            counter += 1
        res=list(str(num1+num2))
        res.reverse()
        ans=temp=ListNode(0) #initialize
        for i in range(len(res)):
            temp.val=res[i]
            if i!=len(res)-1:
                temp.next=ListNode(0)
                temp=temp.next

        return ans




        # arr=[]
        # for i in range(len(res)):
        #     arr.append(ListNode(res[i]))
        # for i in range(len(arr)-1):
        #     arr[i].next=arr[i+1]
        # # print([arr[i].val for i in range(3)])
        # return arr[0]

b=Solution()
b.addTwoNumbers(c,f)