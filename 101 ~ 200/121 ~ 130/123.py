#-*- coding:utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
for 변수 in ["사과", "귤", "수박"]:
    print(변수)
    print("--")
#for문 내의 코드는 세 번 반복 실행됩니다. 변수를 출력하고 이어서 문자열
#("–") 까지 출력합니다.
