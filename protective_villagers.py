def can_place(stalls, k, dist):
    """Return True if we can place k villagers with at least `dist` between them."""
    count = 1
    last_pos = stalls[0]
    for pos in stalls[1:]:
        if pos - last_pos >= dist:
            count += 1
            last_pos = pos
            if count >= k:
                return True
    return False

def max_min_distance(stalls, n, k):
    stalls.sort()
    low = 1
    high = stalls[-1] - stalls[0]
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        if can_place(stalls, k, mid):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans
t=int(input())
for _ in range(t):
    n,c=map(int, input().split())
    arr=list(map(int, input().split()))
    arr.sort()
    b=max_min_distance(arr, n, c)
    print(b)