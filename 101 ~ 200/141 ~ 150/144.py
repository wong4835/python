file_list = ['hello.py', 'ex01.py', 'ch02.py', 'intro.hwp']
for file in file_list :
    temp = file.split('.')
    print(temp[0])
