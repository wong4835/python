#-*- coding:utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
portfolio = ["SK하이닉스", "삼성전자", "LG전자"]
for ticker in portfolio:
    print(ticker, "보유중")
