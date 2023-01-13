n = int(input())

a = list(map(int, input().split()))

maxi = a[0]

for i in a:
    if i > maxi:
        maxi = i

print(maxi)
