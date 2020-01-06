phone_number = input ("휴대전화 번호 입력 : ")
if phone_number[0:3] == "011" :
    print ("당신은 SKT 사용자입니다.")
elif phone_number[0:3] == "016" :
    print ("당신은 KT 사용자입니다.")
elif phone_number[0:3] == "019" :
    print ("당신은 LGT 사용자입니다.")
else :
    print("당신은 알수없는 사용자입니다.")
