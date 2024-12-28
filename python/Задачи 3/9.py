q = 10

def lucky_ticket(n_digits):
    N = n_digits // 2
    S = N * q
    a = (S + 1) * [0]
    a[0] = 1
    for n in range(1 + N):
        for i in range(min(S, n * (q - 1)), 0, -1):
            a[i] = sum(a[ max(0, i + 1 - q) : i + 1 ])

    return sum( x**2 for x in a )

print(lucky_ticket(5))