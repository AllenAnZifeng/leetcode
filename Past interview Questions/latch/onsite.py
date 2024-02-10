


with open('input.csv') as f:
    data = f.read()

data = data.split()
arr = []
for t in data:
    t =t.split(',')
    arr.append((t[0],t[2]))

arr.sort(key = lambda x: x[0])

g = {}
for t in arr:
    if t[0] not in g:
        g[t[0]] = [t[1]]
    else:
        g[t[0]].append(t[1])


for t in arr:
    if t[1] not in g:
        g[t[1]] = [t[0]]
    else:
        g[t[1]].append(t[0])
res = set()
for node,children in g.items():  # node: DAI children: ['USDC', 'USDC', 'FRAX'],
    for child in children: # 'USDC'
        for grandchild in g[child]: #  ['ETH', 'USDT', 'DAI', 'DAI', 'FRAX', 'GPT', 'WBTC'],
            for greatgrandchild in g[grandchild]: # 'ETH': ['USDT', 'ETHM', 'LINK', 'MKR', 'MNT', 'UNI', 'USDC', 'WBTC']
                if greatgrandchild == node:
                    res.add(tuple([node,child,grandchild]))

res = list(res)
res.sort()
# ('ETH', 'USDC', 'WBTC')
# ('WBTC', 'ETH', 'USDC')
# these two are the same, they are rotated, need to eliminate deuplication
exchanges = set()
for combo in list(res):
    a,b,c = combo
    if (b,c,a) not in exchanges and (c,a,b) not in exchanges:
        exchanges.add(combo)


exchanges = list(exchanges)
exchanges.sort()
print(exchanges)

with open('input.csv') as f:
    data = f.read()
data = data.split()
arr = []
for t in data:
    t =t.split(',')
    arr.append(t)
def get_amount_out(amount_in, reserve_in, reserve_out):
    # assert amount_in > 0, 'UniswapV2Library: INSUFFICIENT_INPUT_AMOUNT'
    # assert reserve_in > 0 and reserve_out > 0, 'UniswapV2Library: INSUFFICIENT_LIQUIDITY'
    amount_in_with_fee = amount_in * 997
    numerator = amount_in_with_fee * reserve_out
    denominator = reserve_in * 1000 + amount_in_with_fee
    amount_out = numerator / denominator  # Use integer division for consistency with Solidity
    return amount_out

d = {} # price look up
for t in arr:
    d[(t[0],t[2])] =[float(t[3]),float(t[1])] #
    d[(t[2], t[0])] = [float(t[1]), float(t[3])]

# exchanges = list(exchanges)
# exchanges.sort()
profits = [0]*len(exchanges)

for i,exchange in enumerate(exchanges): #('USDC', 'ETH', 'WBTC')

    for start in range(1,10000):
        temp = get_amount_out(start,d[(exchange[0],exchange[1])][0],d[(exchange[0],exchange[1])][1])
        temp = get_amount_out(temp,d[(exchange[1],exchange[2])][0],d[(exchange[1],exchange[2])][1])
        temp = get_amount_out(temp,d[(exchange[2],exchange[0])][0],d[(exchange[2],exchange[0])][1])
        profits[i] = max(profits[i],temp-start)
print(profits)
