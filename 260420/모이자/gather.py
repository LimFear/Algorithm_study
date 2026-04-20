n = int(input())
A = list(map(int, input().split()))

# Please write your code here.
Min_cnt = 21e8
cnt = 0

for i in range(n):          # 기준점
    for j in range(n):      # 기준점을 두고 최소값을 찾음
        cnt += A[j]*(abs(i-j))

    if cnt < Min_cnt:
        Min_cnt = cnt

    cnt = 0
print(Min_cnt)
