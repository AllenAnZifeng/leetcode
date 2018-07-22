def insert(value, l):
    for i in range(len(l)):
        if i == len(l) - 1:
            l.append(value)
            return None
        if value > l[i] and value < l[i + 1]:
            l.insert(i + 1, value)
            return None
tmp=[1,2,3,5]


insert(4,tmp)
print(tmp)

