k, n, w = map(int, input().split())

price = k * ( (w + 1) * w / 2  ) # Gauss: (1 + 2 + .... + k) * w

if price > n:
    print(int(price) - n)
else:
    print(0)
