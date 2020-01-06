reg_num = input("주민등록번호:")
sum = int(reg_num[0])*2 + int(reg_num[1])*3 + int(reg_num[2])*4 + int(reg_num[3])*5 + int(reg_num[4])*6+ int(reg_num[5])*7 +
      int(reg_num[7])*8 + int(reg_num[8])*9 + int(reg_num[9])*2 + int(reg_num[10])*3 + int(reg_num[11])*4+ int(reg_num[12])*5

# 1차 계산
rem = sum % 11

# 2차 계산
valid_num = 11 - rem

if int(reg_num[13]) == valid_num :
    print("유효한 주민등록번호입니다.")
else :
    print("유효하지 않은 주민등록번호입니다.")
