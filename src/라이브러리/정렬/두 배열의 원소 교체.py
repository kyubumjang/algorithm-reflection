n, k = map(int, input().split()) # n(배열 내 원소의 개수)과 k(바꿀 수 있는 횟수) 입력 받기
a = list(map(int, input().split())) # 배열 A의 모든 원소를 입력 받기
b = list(map(int, input().split())) # 배열 B의 모든 원소를 입력 받기

a.sort() # 배열 A 오름차순 정렬
b.sort(reverse=True) # 배열 B는 내림차순 정렬

# 첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 K번 비교
for i in range(k):
    # A의 원소가 B의 원소봐 작은 경우
    if a[i] < b[i]:
        # 두 원소 교체
        a[i], b[i] = b[i], a[i]
    else: # A의 원소가 B의 원소보다 크거나 같을 때, 반복문 탈출
        break

print(sum(a)) # 배열 A의 모든 원소의 합을 출력


