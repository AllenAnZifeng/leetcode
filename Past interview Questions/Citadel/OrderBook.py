"""
Some background info:
    * You don't need to worry about how BUY and SELL orders are matched. 
      For the purpose task, treat them as independent parts that do not interact with each other.
    * Order IDs of orders in an order book should be unique.
"""
from enum import Enum


# Enum Representing Side of the Order
class Side(Enum):
    BUY = 1
    SELL = 2

# Class Representing an Order
class Order:
    """
    Initialize an Order
    """
    def __init__(self, id: int, side: Side, price: int, quantity: int) -> None:
        # Unique id of an order
        self.id = id
        # The side the order is on
        self.side = side
        # Price of the order for each share
        self.price = price
        # Number of shares to be executed in this order
        self.quantity = quantity


# Class Representing an Order Book for a particular stock
class OrderBook:
    """
    Initialize an Order Book
    """
    def __init__(self) -> None:
        self.orders = {} # id: Order object
        self.buy_prices:dict[int,int] = {}
        self.sell_prices: dict[int, int] = {}  # price : total quantity in book

    """
    Send order to the order book. Return True if the operation is success, return False otherwise.
    If order has an id that already exist in the order book, do not modify the original order and tread it as a failure case.
    """
    def sendOrder(self, order: Order) -> bool:
        if order.id in self.orders:
            return False

        self.orders[order.id] = order
        if order.side == Side.BUY:
            if order.price not in self.buy_prices:
                self.buy_prices[order.price] = 0
            self.buy_prices[order.price] += order.quantity
        else:
            if order.price not in self.sell_prices:
                self.sell_prices[order.price] = 0
            self.sell_prices[order.price] += order.quantity

        return True

    """
    Delete the order with order id. Return True if the operation is successful.
    """
    def deleteOrder(self, id: int) -> bool:
        if id in self.orders:
            order = self.orders[id]
            if order.side == Side.BUY:
                self.buy_prices[order.price] -= order.quantity
                if self.buy_prices[order.price] == 0:
                    del self.buy_prices[order.price]
            else:
                self.sell_prices[order.price] -= order.quantity
                if self.sell_prices[order.price] == 0:
                    del self.sell_prices[order.price]


            del self.orders[id]
            return True
        else:
            return False

    """
    Return the quantity of the stock in the order book for the side and price. 
    Only return the quantity for orders with the exact price.
    """
    def getQuantityForPrice(self, side: Side, price: int) -> int:


        if side == Side.BUY:
            if price not in self.buy_prices:
                return 0
            else:
                return self.buy_prices[price]
        else:
            if price not in self.sell_prices:
                return 0
            else:
                return self.sell_prices[price]





    """
    Return the quantity of the stock in the order book for the side and the next best price.
    The next best price is defined as:
        The smallest price greater than price for BUY
        The greatest price smaller than price for SELL
    """
    @staticmethod
    def bs_bigger_than_val(arr, val):
        l, r = 0, len(arr) - 1
        res = 0
        while l <= r:
            m = (l + r) // 2
            if arr[m] <= val:
                l = m + 1
                res = l
            else:
                r = m - 1
        return res
    def getQuantityForNextBestPrice(self, side: Side, price: int) -> int:
        if side == Side.BUY:
            pass



#
# arr = [3,4,6,7,8]
# # arr=[4,5]
arr= [1]
# val = 5

def bs(arr,val):
    l, r = 0, len(arr) - 1
    m = 0
    while l <= r:
        m = (l + r) // 2
        if arr[m] > val:
            r = m -1
        elif arr[m] < val:
            l = m +1
        else:
            return m
    return m,'not found'

# print(bs(arr,5))
def bs_bigger_than_val(arr,val):
    l,r = 0,len(arr)-1
    res = 0
    while l<=r:
        m = (l+r) // 2
        if arr[m] <= val:
            l = m+1
            res = l
        else:
            r = m-1
    print('index',res)
    return res
# print(bs_bigger_than_val(arr,val))

def bs_smaller_than_val(arr,val):
    l, r = 0, len(arr) - 1
    res = r
    while l <= r:
        m = (l + r) // 2
        if arr[m] >= val:
            r = m -1
            res = r
        else:
            l = m+1
    return res

# print(bs_smaller_than_val(arr,val))


def binary_search_insert(ordered_list, new_element):
    left, right = 0, len(ordered_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if ordered_list[mid] < new_element:
            left = mid + 1
        else:
            right = mid - 1
    ordered_list.insert(left, new_element)

# Example usage
ordered_list = [1, 2, 4,  7, 8]
new_element = 6
binary_search_insert(ordered_list, new_element)
print(ordered_list)