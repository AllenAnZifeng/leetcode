
xs = [1,2,3] # sorted
ys = [1,1,3]

fx = {}
fy = {}
for x in xs:
    if x not in fx:
        fx[x] = 0
    fx[x] +=1

for y in ys:
    if y not in fy:
        fy[y] = 0
    fy[y] +=1


y_combo = 0
for i in range(len(ys)):
    num = ys[i]
    y_combo += i + fy[num]
    fy[num] -=1

x_combo = 0
for i in range(len(xs)):
    num = xs[i]
    x_combo += i + fx[num]
    fx[num] -=1

print(y_combo,x_combo)