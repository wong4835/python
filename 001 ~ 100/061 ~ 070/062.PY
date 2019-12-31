#-*- coding:utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')interest_0 = ['삼성전자', 'LG전자', 'SK Hynix']
interest_1 = interest_0[:2]
interest_1[0] = 'Naver'
print(interest_0)
#리스트의 슬라이싱은 리스트를 복사 생성합니다. interest_0과 interest_1은 별도의 공간에 각각의 값이 저장되어 있습니다. 따라서, interest_1의 값을 수정해도 interest_0의 값이 변경되지 않습니다.

['삼성전자', 'LG전자', 'SK Hynix']
