num = [("jam",2),("dub",4)]
core = 0
for unity in num:
    core += unity[1]

print(core)

aka = sum(a[0] for a in num)