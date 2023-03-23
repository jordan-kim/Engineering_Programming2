#학번  2019072506
#이름 이종건
list1 = list(input('주민등록번호 -와 함께 입력:'))

year = ''.join(list1[0:2])
month = ''.join(list1[2:4])
day = ''.join(list1[4:6])

if list1[7] == '1':
  print('나는 19{}년 {}월 {}일에 태어난 남자입니다'.format(year,month,day))

elif list1[7] == '2':
  print('나는 19{}년 {}월 {}일에 태어난 여자입니다'.format(year,month,day))

elif list1[7] == '3':
  print('나는 20{}년 {}월 {}일에 태어난 남자입니다'.format(year,month,day))

elif list1[7] == '4':
  print('나는 20{}년 {}월{}일에 태어난 여자입니다'.format(year,month,day))







#############################################################


#파일 이름은 자신의 학번, 이름으로 설정해주세요.