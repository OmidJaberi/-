a, b, l = map(int, input().split())

ans = int(l / 2) * (a + b)
if l % 2 == 1:
    ans += a
print(ans)
