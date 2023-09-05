n = int(input())
product_no_list = set(map(int, input().split()))

m = int(input())
target_no_list = list(map(int, input().split()))

for i in target_no_list:
    if i in product_no_list:
        print('yes', end=' ')
    else:
        print('no', end=' ')