T = int(input())
for t in range(T):
    N = int(input())
    P = input()
    ans = ""
    for p in P:
        ans += 'S' if p == 'E' else 'E'
    print("Case #{}: {}".format(t+1, ans))