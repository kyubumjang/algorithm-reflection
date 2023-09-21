# 이진 탐색 소스코드 구현(반복문)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(input())
product_no_array = list(map(int, input().split()))
product_no_array.sort()

m = int(input())
target_no_array = map(int, input().split())

for i in target_no_array:
    # 해당 부품 존재하는지 확인
    result = binary_search(product_no_array, i, 0, n - 1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')

