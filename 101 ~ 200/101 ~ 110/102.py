#-*- coding:utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
숫자를 입력하세요: 30
user_data = int(input("숫자를 입력하세요:"))
print(user_data + 10)
