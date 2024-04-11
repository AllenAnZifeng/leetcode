

class A:
    def __init__(self,val):
        self.val = val
        self.name = 'a'

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return self.__str__()


def sort_f(x:A):
    return x.val

a = A(1)
b = A(2)
arr: [A] = [a,b]

print(a)

arr.sort(key=sort_f)
print(arr)