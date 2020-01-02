#-*- coding:utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
inventory = {'메로나': [300, 20], '비비빅': [400, 3], '죠스바': [250, 100]}
print('메로나')
item = inventory['메로나']
print(item[0], '원')
item = inventory['메로나']
print(item[1], '개')
print('비비빅')
item = inventory['비비빅']
print(item[0], '원')
item = inventory['비비빅']
print(item[1], '개')
print('죠스바')
item = inventory['죠스바']
print(item[0], '원')
item = inventory['죠스바']
print(item[1], '개')
