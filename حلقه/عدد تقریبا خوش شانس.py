n = input()

cnt = 0

for i in n:
    if i == '4' or i == '7':
        cnt += 1

ans = True
if cnt == 0:
    ans = False

while cnt > 0:
    if cnt % 10 != 7 and cnt % 10 != 4:
        ans = False
    cnt = int(cnt / 10)

if ans:
    print("YES")
else:
    print("NO")
