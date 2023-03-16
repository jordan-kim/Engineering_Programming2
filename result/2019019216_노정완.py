#학번
#이름
# 2019019216
# 노정완
#############################################################
#코드
ssn = input("주민등록번호를 입력하세요 (YYMMDD-1234567): ")     # 주민등록번호를 입력받음

birth, gen = ssn.split("-")    # birth와 gen을 -로 구분해서 받음

birth_year = birth[:2]      # birth의 년도 부분을 지정
birth_month = birth[2:4]    # birth의 월 부분을 지정
birth_day = birth[4:6]      # birth의 일 부분을 지정

if gen[0] in ["1", "3"]:    # gen부분의 첫 글자가 1 or 3이면
    gender = "남자"          # 성별을 "남자"로 지정
else:                       # gen부분의 첫 글자가 1 or 3이 아니면
    gender = "여자"          # 성별을 "여자"로 지정

if gen[0] in ["1", "2"]:    # gen의 글자가 1 or 2이면
    birth_year = "19" + birth_year  # birth_year에 1900년대로 바꾸어줌
else:                       # 아니라면
    birth_year = "20" + birth_year  # birth_year에 2000년대로 바꾸어줌

print(f"나는 {birth_year}년 {birth_month}월 {birth_day}일에 태어난 {gender}입니다.")    # 결과값 출력

#############################################################


#파일 이름은 자신의 학번, 이름으로 설정해주세요.