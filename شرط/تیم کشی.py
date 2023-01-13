a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
a3 = int(input())
b3 = int(input())

ans = 0

if a1 < b1:
    ans += a1
else:
    ans += b1

if a2 < b2:
    ans += a2
else:
    ans += b2

if a3 < b3:
    ans += a3
else:
    ans += b3

print(ans)
