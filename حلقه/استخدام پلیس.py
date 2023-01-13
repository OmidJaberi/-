n = int(input())
a = list(map(int, input().split()))

p = 0
ans = 0

for i in a:
    if i == -1 and p == 0:
        ans += 1
    else:
        p += i

print(ans)
