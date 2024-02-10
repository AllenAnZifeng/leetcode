#
# def f(graph):
#     d = {}
#     for k,v in graph:
#         if k not in d:
#             d[k] = [v]
#         else:
#             d[k].append(v)
#     return recursive(0,d)
# def recursive(node, d):
#
#     if node not in d or len(d[node]) == 0:
#             return 0
#
#     arr = [recursive(i,d) for i in d[node]]
#
#     arr.sort(reverse=True)
#
#     print(node, arr)
#
#     arr = [arr[i] + i +1 for i in range(len(arr))]
#
#     print(node,arr)
#
#     return max(arr)
#
# if __name__ == '__main__':
#     graph =  [[0, 1], [0, 2], [0, 3], [1, 4], [2, 5], [2, 6], [3, 7],[5,8]]
#     print(f(graph))


def f(graph):
    d = {}
    for k, v in graph:
        if k not in d:
            d[k] = [v]
        else:
            d[k].append(v)

    return d


def recursive(node, d) -> int:
    if node not in d:
        return 0

    res = [recursive(n, d) for n in d[node]]

    res = sorted(res, reverse=True)
    print(node, res)

    res = [res[i] + 1 + i for i in range(len(res))]

    return max(res)


def recursive2(node, d) -> int:
    if node not in d:
        return 0

    res = [recursive(n, d) for n in d[node]]

    print(node, res)

    # res = [res[i]+1+i for i in range(len(res))]

    return max(max(res) + 1, len(d[node]))


if __name__ == '__main__':
    graph = [[0, 1], [0, 2], [0, 3], [1, 4], [2, 5], [2, 6], [3, 7], [5, 8]]
    d = f(graph)

    print(recursive(0, d))
    print(recursive2(0, d))
