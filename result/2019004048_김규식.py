# 학번 2019004048
# 이름 김규식
# commit에 수정한 내역을 적어서 다시 commit 합니다..

#############################################################
# 코드
# 입력 받기
number = input("주민등록 번호를 입력하세요")
# 슬라이싱 후 정수 변환
number_year = int(number[0:2])
number_month = int(number[2:4])
number_day = int(number[4:6])
number_gender = int(number[7])

# 출력시 달라지는 부분
if number_gender == 1:
    gender = "남자"
    number_year += 1900
if number_gender == 2:
    gender = "여자"
    number_year += 1900
if number_gender == 3:
    gender = "남자"
    number_year += 2000
if number_gender == 4:
    gender = "여자"
    number_year += 2000

#출력
print("나는 {}년 {}월 {}일에 태어난 {}입니다.".format(number_year, number_month, number_day, gender))

#############################################################


#파일 이름은 자신의 학번, 이름으로 설정해주세요.