n = int(input())
time_list = list(map(int, input().split()))
total_time = 0

time_list.sort()

for i in range(1, n+1):
    total_time += sum(time_list[0:i])

print(total_time)

# 3 1 4 3 2
# 1 2 3 3 4
