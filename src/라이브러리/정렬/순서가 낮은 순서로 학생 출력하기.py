# 학생 수 n 입력 받음
n = int(input())

# n명의 학생 정보를 입력받아 리스트에 저장
student_info = []
for i in range(n):
    input_data = input().split()
    # 이름은 문자열 그대로  점수는 정수형으로 변환하여 저장
    student_info.append((input_data[0], int(input_data[1])))

# 키를 이용하여 점수를 기준으로 정렬
student_info = sorted(student_info, key=lambda student: student[1])

# 정렬이 수행된 결과를 출력
for student in student_info:
    print(student[0], end=" ")