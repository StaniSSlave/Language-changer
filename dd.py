a = list(input())
for i in range(1,len(a),10):
    p = 0
    while p == 0:
        c, t = a[i], a[i+5]
        a[i] = t
        a[i+5] = c
        a_upd = "".join(a)
        p = 1
        print(a_upd)