# 2019075714
# 정명진

#############################################################
#코드
p_number=input('주민등록번호를 입력하세요 : ')
year=p_number[0]
if int(year)==9:
    year='19'+p_number[0:2]
else:
    year='20'+p_number[0:2]
month=p_number[2:4]
day=p_number[4:6]
if int(p_number[7]) in [1,3]:
    gender='남자'
else:
    gender='여자'
print('나는 {}년 {}월 {}일에 태어난 {}입니다.'.format(year,month,day,gender))
#############################################################
#파일 이름은 자신의 학번, 이름으로 설정해주세요.