# import time
#
# def log_args(func):
#     def wrapper(*args, **kwargs):
#         print(f"log args")
#         return func(*args, **kwargs)
#     return wrapper
#
# def timing(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#
#         end_time = time.time()
#         print(f"timing")
#         result = func(*args, **kwargs)
#         return result
#     return wrapper
#
# # @timing
# # @log_args
# def some_function(a, b):
#     time.sleep(0.1)  # Simulate a time-consuming operation
#     return a + b
#
# # print(some_function(5, 3))
# print(timing(log_args(some_function))(5, 3))
#
# # some_function(5, 3)


# obj = 's'
# print(dir(obj))

# for att in dir(obj):
#     print(att, getattr(obj, att))
class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(People):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def getgrade(self):
        return self.grade

# check student parent class
print(Student.__bases__)


