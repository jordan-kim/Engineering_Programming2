#학번
#2020037392

#이름
#김유정

#############################################################
#코드

#주민번호 입력
ID_number = input('예 : 981216-1234123 입력 -> ')

#년도 알아내기
birth_year = int(ID_number[0:2])

#성별 알아내기
gender_year = int(ID_number[-7])
gender = '남자' if gender_year == 1 or gender_year == 3 else '여자'

#90, 00년생 판별
if 0 <= birth_year <= 23:
    birth_year_num = birth_year +  2000

if 24<= birth_year <= 99:
    birth_year_num = birth_year + 1900

##출력하기
print (f'나는 {birth_year_num}년 {ID_number[2:4]}월 {ID_number[4:6]}일에 태어난 {gender}입니다.')

#############################################################


#파일 이름은 자신의 학번, 이름으로 설정해주세요.