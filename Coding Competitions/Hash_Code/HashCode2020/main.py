from functools import reduce
from typing import List, Dict, Tuple


class Book:
    def __init__(self, id: int, score: int):
        self.id = id
        self.score = score
        self.scanned = False

    def __str__(self):
        return "<Book %d>(score:%d)" % (self.id, self.score)

    def __repr__(self):
        return str(self)


class Lib:
    def __init__(self, id: int, signup_days: int, books_each_day: int):
        self.id = id
        self.books: Dict[int, Book] = dict()

        self.signup_days = signup_days
        self.books_each_day = books_each_day
        self.active = False

    def __str__(self):
        return "<Lib %d>(active:%s,sign:%d,per day:%d)%s" % (
            self.id, self.active, self.signup_days, self.books_each_day, str(self.books))

    def __repr__(self):
        return str(self)

    def book_length_output(self, days_remain: int) -> Tuple[int, int]:
        return (days_remain - self.signup_days) * self.books_each_day, len(
            [b for b in self.books.values() if not b.scanned])

    def total_value(self, days_remain: int) -> int:
        possible_output, remain_books = self.book_length_output(days_remain)
        total_score = 0
        if possible_output <= remain_books:
            self.books = {k: v for k, v in sorted(self.books.items(), key=lambda a: a[1].score if not a[1].scanned else 0, reverse=True)}
            count = 0
            for k, v in self.books.items():
                if not v.scanned:
                    if count >= possible_output:
                        break
                    total_score += v.score
                    count += 1
        else:
            total_score = sum([b.score for b in self.books.values() if not b.scanned])
        return total_score


class Task:

    def __init__(self, days: int, books: Dict[int, Book] = None, libs: Dict[int, Lib] = None):
        self.results: Dict[int, List[int]] = dict()  # lib_id: [book_ids]
        self.lib_orders = []

        self.days = days
        self.days_remain = days
        if libs is None:
            libs = dict()
        if books is None:
            books = dict()
        self.books = books
        self.libs = libs

        self.lib_activating: Lib = None
        self.activation_remain: int = 0

    def pick_lib(self) -> Lib:
        max_lib = None
        max_score = 0
        for lib in [l for l in self.libs.values() if not l.active]:
            score = lib.total_value(self.days_remain - int(lib.signup_days * 3.5))
            if score >= max_score:
                max_lib = lib
                max_score = score
        return max_lib

    def scan(self, lib_index: int, book_index: int):
        self.books[book_index].scanned = True
        # add book to result
        if not lib_index in self.results:
            self.results[lib_index] = []
        self.results[lib_index].append(book_index)

    def activate(self, lib: Lib):
        print('Activating %d' % lib.id)
        self.lib_orders.append(lib.id)

        self.lib_activating = lib
        self.activation_remain = lib.signup_days


        for book_index in lib.books.keys():
            self.scan(lib.id, book_index)

    def update(self):

        if self.lib_activating:
            # if the previous lib is activated
            if self.activation_remain == 0:
                self.lib_activating.active = True
                self.lib_activating = None
                # pick lib
                self.lib_activating = self.pick_lib()
                self.activate(self.lib_activating)
            else:
                self.activation_remain -= 1
        else:
            # pick lib
            self.lib_activating = self.pick_lib()
            self.activate(self.lib_activating)
        self.days_remain -= 1

    def get_result(self):
        output = ''

        output += str(len(self.results)) + '\n'

        for lib_index in self.lib_orders:
            output += "%d %d\n" % (lib_index, len(self.results[lib_index]))
            output += ' '.join(map(str, self.results[lib_index]))
            output += '\n'

        return output


if __name__ == '__main__':
    path = 'e_so_many_books.txt'
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
        while len(content) and content[0] != '\n':
            _, signup_days, books_each_day = [int(s) for s in content.pop(0).strip('\n').split(' ')]
            lib = Lib(lib_index, signup_days, books_each_day)
            lib.books = {i: task.books[i] for i in [int(s) for s in content.pop(0).split(' ')]}
            task.libs[lib_index] = lib
            lib_index += 1

        # for book in task.books.values():
        #     print(book)
        #
        # for lib in task.libs.values():
        #     print(lib)

        # print('=========================')

        while task.days_remain > 0:
            task.update()

        result = task.get_result()
        print(result)
        with open(path + '.out.txt', mode='w') as f:
            f.write(result)



