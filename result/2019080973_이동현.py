#학번 2019080973
#이름 이동현


#############################################################
#코드 yymmdd-xxxxxxx
print("생일과 주민번호를 입력하십시오")
A = input()
B = int(A[0:2])
B1 = int(A[2:4])
B2 = int(A[4:6])
C = int(A[7])
if B <= 23 :
    B += 2000
    if C == 3 :
        print("나는 ".strip(),B,"년 ".rstrip(),B1,"월 ".rstrip(),B2,"일에 태어난 남자입니다.")
    if C == 4 :
        print("나는 ", B, "년 ", B1, "월 ", B2, "일에 태어난 여자입니다.")
if B > 23 :
    B += 1900
    if C == 1 :
        print("나는 ", B, "년 ", B1, "월 ", B2, "일에 태어난 남자입니다.")
    if C == 2 :
        print("나는 ", B, "년 ", B1, "월 ", B2, "일에 태어난 여자입니다.")







#############################################################


#파일 이름은 자신의 학번, 이름으로 설정해주세요.