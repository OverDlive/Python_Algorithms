import time

data = input()
result = int(data[0])

start_time = time.time()

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)

end_time = time.time()

print("time:", end_time-start_time)