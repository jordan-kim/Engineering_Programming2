#학번 2019060764
#이름 서재윤


#############################################################
#코드
try:
    i = input('주민번호를 입력하세요(예000101-3011111):')
    a = i.split('-')
    b = a[0]
    c = a[1]
    print(b)
    year = int(b[0:2])
    month = int(b[2:4])
    day = int(b[4:6])
    gender = int(c[0:1])
    if gender == 1 or gender == 2:
        full_y = 1900 + year
    else:
        full_y = 2000 + year
    if gender == 1 or gender == 3:
        gen = '남자'
    else:
        gen = '여자'
    print('나는 ', full_y, '년 ', month, '월 ', day, '일에 태어난 ', gen, '입니다.', sep='')
except:
    print('잘못된 번호를 입력하셨습니다.')


#############################################################


#파일 이름은 자신의 학번, 이름으로 설정해주세요.