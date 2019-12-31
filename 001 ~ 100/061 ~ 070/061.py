#-*- coding:utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
interest_0 = ['삼성전자', 'LG전자', 'SK Hynix']
interest_1 = interest_0
interest_1[0] = 'Naver'
print(interest_0)
#interest_0은 interest_1와 값이 같게 한뒤 interest_1에서 첫번째것을
#Naver로 바꾸어서 출력해서 ['Naver', 'LG전자', 'SK Hynix']이나오는 것이다.
