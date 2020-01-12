my_list = ["A", "b", "c", "D"]
for val in my_list :
    if val.isupper() :
        print(val.lower(), end='')
    else :
        print(val.upper(), end='')
