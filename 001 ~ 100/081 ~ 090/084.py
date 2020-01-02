#-*- coding:utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
inventory = {'메로나': [300, 20], '비비빅': [400, 3], '죠스바': [250, 100]})
inventory['월드콘'] = [500, 7])
print(inventory)
