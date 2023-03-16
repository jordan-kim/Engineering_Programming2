#학번 2019030455
#이름 고주환

#############################################################
#코드
jumin_num = input("주민등록번호를 입력하세요 (예: 123456-1234567): ")

# 입력한 주민등록번호가 유효한지 체크
if len(jumin_num) != 14 or jumin_num[6] != '-':
    print("잘못된 입력입니다. 주민등록번호를 다시 입력해주세요.")
else:
    # 생년월일 추출
    year = int(jumin_num[:2])
    month = int(jumin_num[2:4])
    day = int(jumin_num[4:6])

    # 세기 추출
    century=0
    gender_num = int(jumin_num[7])
    if gender_num == 1 or gender_num == 2:
        century = 1900
    elif gender_num == 3 or gender_num == 4:
        century = 2000

    # 성별 추출
    if gender_num % 2 == 1:
        gender = '남자'
    elif gender_num % 2 == 0:
        gender = '여자'
    else:
        gender = '알 수 없음'

    # 출생년도 계산
    birth_year = century + year

    # 메세지 출력
    print("나는 {}년 {}월 {}일에 태어난 {}입니다.".format(birth_year, month, day, gender))

#############################################################


#파일 이름은 자신의 학번, 이름으로 설정해주세요.