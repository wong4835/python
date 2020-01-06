user_in = input()
if user_in.islower():
    user_in = user_in.upper()
else :
    user_in = user_in.lower()
print(user_in)user_in = input("제가좋아하는계절은:")
if user_in in fruit.keys() :
    print("정답입니다")
else :
    print("오답입니다")
