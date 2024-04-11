from os import *
from sys import *
from collections import *
from math import *

from typing import List


class Node:
    def __init__(self):
        self.children = {}
        self.end = False
        self.hot = -1


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str, hot: int):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.end = True
        cur.hot = hot

    def startwith(self, word) -> List[str]:
        cur = self.root
        res = []  # (prefix, hot)
        for c in word:
            if c not in cur.children:
                return []
            cur = cur.children[c]

        prefix = word
        for char, node in cur.children.items():
            self.dfs(node, prefix + char, res)

        res.sort(key=lambda x: (-x[1], x[0]))

        return [word for word, hot in res][:3]

    def dfs(self, node: Node, prefix: str, res: List[str]):
        if node.end:
            res.append((prefix, node.hot))
        for char, nxt_node in node.children.items():
            self.dfs(nxt_node, prefix + char, res)


class AutocompleteSystem:

    def __init__(self, sentences, times):
        self.prefix = ''
        self.trie = Trie()
        for sentence, time in zip(sentences, times):
            self.trie.insert(sentence, time)

    def input(self, c: chr) -> List[str]:
        # write your code here
        if c == '#':
            return []

        self.prefix += c
        return self.trie.startwith(self.prefix)


sentences = '''lrawwjjmb
meretllhgv
mprvaprhcpi
mmwhoviooe
mpmetrunngjht
mpmevahgudpli
mpmvuwqgbqsm
mpqeotictew
ewbtisbtj
momnqgtddm'''
sentences=sentences.split()

times = '9 6 9 11 8 7 9 10 7 10'
times=times.split()
times = [int(t) for t in times]


print(sentences)
print(times)

inputs = 'mpmehv#'
autocomplete = AutocompleteSystem(sentences,times)
for c in inputs:
    print(autocomplete.input(c))





