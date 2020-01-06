zipcode = input("우편번호:")
if zipcode[2] in "012" :
    print("강북구")
elif zipcode[2] in "345" :
    print("도봉구")
else :
    print("노원구")
