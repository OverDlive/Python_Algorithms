import time

start_time = time.time()

n, m = map(int, input().split())
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)

end_time = time.time()

print('time:',end_time-start_time)