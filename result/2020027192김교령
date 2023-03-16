#2020027192
#김교령


#############################################################
#코드

r_number = input('주민등록번호를 입력해주세요: ')
b_year = r_number[:2]
b_month = r_number[2:4]
b_day = r_number[4:6]
gender = r_number[7]

if gender == '1' or gender == '2':
    year = '19' + b_year
elif gender == '3' or gender == '4':
    year = '20' + b_year
else:
    print('올바른 주민등록번호를 입력하세요.')
    exit()

if gender == '1' or gender == '3':
    gender_text = '남자'
else:
    gender_text = '여자'

print('나는 {}년 {}월 {}일에 태어난 {}입니다.'.format(year, b_month, b_day, gender_text))


#############################################################


#파일 이름은 자신의 학번, 이름으로 설정해주세요.
