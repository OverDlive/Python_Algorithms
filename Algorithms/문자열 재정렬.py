from curses.ascii import isalpha
import time

start_time = time.time()

data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()

if value != 0:
    result.append(str(value))

print(result)

end_time = time.time()

print('time:', end_time-start_time)