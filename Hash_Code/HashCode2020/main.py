from functools import reduce
from typing import List


class Book:
   def __init__(self, id: int, score: int):
       self.id = id
       self.score = score

   def __str__(self):
       return "<Book %d>(score:%d)" % (self.id, self.score)

   def __repr__(self):
       return str(self)


class Lib:
   def __init__(self, id: int, signup_days: int, books_each_day: int):
       self.id = id
       self.books = dict()
       self.signup_days = signup_days
       self.books_each_day = books_each_day
       self.active = False

   def __str__(self):
       return "<Lib %d>(active:%s,sign:%d,per day:%d)%s" % (
           self.id, self.active, self.signup_days, self.books_each_day, str(self.books))

   def __repr__(self):
       return str(self)

   def book_output(self, days_remain: int) -> int:
       return min((days_remain - self.signup_days) * self.books_each_day, len(self.books))

   def total_value(self) -> int:
       return sum([book.score for book in self.books.values()])


class Task:
   def __init__(self, days: int, books=None, libs=None):
       self.days = days
       self.days_remain = days
       if libs is None:
           libs = dict()
       if books is None:
           books = dict()
       self.books = books
       self.libs = libs


if __name__ == '__main__':
   path = 'a_example.txt'
   task = None

   with open(path) as f:
       content = f.readlines()

       # skip first line
       _, _, days = [int(s) for s in content.pop(0).split(' ')]
       task = Task(days)

       # parse books
       book_index = 0
       for score in [int(s) for s in content.pop(0).split(' ')]:
           task.books[book_index] = Book(book_index, score)
           book_index += 1

       # parse libs
       lib_index = 0
       while len(content):
           _, signup_days, books_each_day = [int(s) for s in content.pop(0).split(' ')]
           lib = Lib(lib_index, signup_days, books_each_day)
           lib.books = {i: task.books[i] for i in [int(s) for s in content.pop(0).split(' ')]}
           task.libs[lib_index] = lib
           lib_index += 1

       print(str(task.books))
       print(str(task.libs))


