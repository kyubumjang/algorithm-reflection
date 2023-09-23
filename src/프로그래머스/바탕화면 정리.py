# 저장해둔 파일 삭제
# 바탕화면의 상태를 나타낸 문자열 배열 wllpaper
# 가장 왼쪽 위 (0, 0)
# 빈칸은 '.' 파일이 있는 칸은 '#'
# 드래그 하면 파일 선택, 선택된 파익 삭제 가능
# 최소한의 이동거리를 가지는 한번의 드래그로 모든 파일 삭제
# 왼쪽 버튼을 클릭한 상태로 드래그한 뒤 마우스 왼쪽 버튼을 떼는 행동
# 점 S에서 점 E로 드래그한다. => 점 S와 점 E를 각각 드래그의 시작점 끝점
# 그래그한 거리는 (rdx - lux) + (rdy - luy)
# 드래그의 시작점과 끝점을 담은 정수배열
# 시작점(lux, luy) 끝점(rdx, rdy) => [lux, luy, rdx, rdy]
def solution(wallpaper):
    answer = []
    rdx = 0
    rdy = 0
    lux = 0
    luy = 0
    count = 0
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                if count == 0:
                    lux = i
                    luy = j
                    rdx = i
                    rxy = j
                print(lux, luy)
                lux = min(lux, i)
                luy = min(luy, j)
                rdx = max(rdx, i + 1)
                rdy = max(rdy, j + 1)
                count += 1

    answer.append(lux)
    answer.append(luy)
    answer.append(rdx)
    answer.append(rdy)

    return answer