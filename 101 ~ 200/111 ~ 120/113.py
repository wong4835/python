user_in = input("입력:").split()

amount = user_in[0]
currency = user_in[1]

if currency == "달러" :
    ratio = 1167
elif currency == "엔" :
    ratio = 1.096
elif currency == "유로" :
    ratio = 1268
else :
    ratio = 171
print(ratio * int(amount), "원")
