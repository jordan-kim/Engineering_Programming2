#학번 2019046362
#이름 조경진

#############################################################
#코드
a=0
b=0
while True:
    a, b = input("주민등록번호를 입력해주세요 :").split("-")
    if int(a[0:2])>23:
        if int(b[0]) == 1:
            print("나는 {}년 {}월 {}일에 태어난 남자입니다.".format("19"+a[0:2],a[2:4],a[4:]))
        elif int(b[0]) == 2:
            print("나는 {}년 {}월 {}일에 태어난 여자입니다.".format("19"+a[0:2],a[2:4],a[4:]))
        else:
            continue

    else:
        if int(b[0]) == 3:
            print("나는 {}년 {}월 {}일에 태어난 남자입니다.".format("20" + a[0:2], a[2:4], a[4:]))
        elif int(b[0]) == 4:
            print("나는 {}년 {}월 {}일에 태어난 여자입니다.".format("20" + a[0:2], a[2:4], a[4:]))
        else:
            continue




#############################################################


#파일 이름은 자신의 학번, 이름으로 설정해주세요.