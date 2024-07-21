
from typing import List

class Node:
    def __init__(self,name) -> None:
        self.name = name
        self.next = []


def dfs(cur_node:Node,path:List[str]):
    if len(path) == 0:
        print(cur_node.name)
    else:
        print(''.join(path[:-1]+['--']+[cur_node.name]))
    
    if len(path) >= 2 and path[-2] == '\\':
        path[-2] = ' '
    for child in cur_node.next[:-1]:
        dfs(child,path + ['|'] +['  '])
    
    if len(cur_node.next) >0:
        dfs(cur_node.next[-1],path + ['\\'] +['  '])



etc = Node('etc')
apache2 = Node('apache2')
extra1 = Node('extra')
extra2 = Node('extra')
original = Node('original')
asl = Node('asl')
cups = Node('cups')
abc = Node('abc')

etc.next.append(apache2)
etc.next.append(asl)
etc.next.append(cups)

apache2.next.append(extra1)
apache2.next.append(original)
original.next.append(extra2)
extra2.next.append(abc)


periodic = Node('periodic')
weekly = Node('weekly')
daily = Node('daily')
one = Node('one')
two = Node('two')
three = Node('three')
alpha = Node('alpha')
beta = Node('beta')
monthly = Node('monthly')

etc.next.append(periodic)
periodic.next.append(weekly)
weekly.next.append(daily)
daily.next.append(one)
daily.next.append(two)
daily.next.append(three)
three.next.append(alpha)
three.next.append(beta)
weekly.next.append(monthly)


dfs(etc,[])

