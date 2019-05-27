n = 1
for i in range(0, 5):
    for j in range(0, i + 1):
        print(n, end="")
        n = n + 1
    print('')

for i in range(0, 5):
    num = 1
    for j in range(0, i + 1):
        print(num, end="")
        num = num + 1
    print('')

val = 65
for i in range(0, 5):
    for j in range(0, i + 1):
        ch = chr(val)
        print(ch,end="")
        val = val + 1
    print('')

