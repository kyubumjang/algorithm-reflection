# 맵 세로 n, 가로 m  (3<= N, m<=50)
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
# 리스트 컴프리헨션 문법 사용하여 2차원 리스트 초기화
d = [[0] * m for _ in range(n)]

# 현재 캐릭터의 칸 좌표 (a, b), 바라보고 있는 방향 d
x, y, direction = map(int, input().split())

# 현재 좌표 방문 처리
d[x][y] = 1

# 전체 맵 정보 입력받기 - 육지가 0 바다가 1
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북 - 0, 동 - 1 남 - 2, 서 -3 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# 왼쪽으로 회전
def turn_left():
    global direction  # global 키워드를 사용한 이유는 정수형 변수인 direction 변수가 함수 바깥에서 선언된 전역변수이기 때문이다.
    direction -= 1
    if direction == -1:
        direction = 3


# 시뮬레이션 시작
count = 1  # 방문한 칸의 개수
turn_time = 0

while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전 후 가보지 않은 칸이 존재한다면 한 칸 전진
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue

    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1

    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀 있는 경우
        else:
            break
        turn_time = 0
# 네 방향 모두 이미 가본 칸이거나 바다인 경우 바라보는 방향은 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다.(단 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우 움직임을 멈춘다.
print(count34)