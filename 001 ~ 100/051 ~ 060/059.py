#-*- coding:utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
string = "삼성전자/LG전자/Naver"interest = []
interest.append(string[0:4])
interest.append(string[5:9])
interest.append(string[10:15])
