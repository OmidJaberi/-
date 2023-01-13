n = int(input())
m = n

reverse = 0

while m > 0:
    reverse = 10 * reverse + m % 10
    m = int(m / 10)

if reverse == n:
    print("YES")
else:
    print("NO")
