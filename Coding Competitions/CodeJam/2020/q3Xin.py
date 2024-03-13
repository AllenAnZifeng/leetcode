inputs = """5
0000
101
111000
1
312
""".split("\n")

def input():
    return inputs.pop(0)


for case_num in range(int(input())):
    output = ""
    n = 0
    diff = 0
    for c in input():
        diff = int(c) - n
        n = int(c)
        if diff > 0:
            output += "(" * diff
        elif diff < 0:
            output += ")" * -diff
        output += c
    if n > 0:
        output += ")" * n
    print("Case #" + str(case_num+1) + ": " + output)