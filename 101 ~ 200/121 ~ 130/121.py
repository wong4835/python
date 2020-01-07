#-*- coding:utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
for 변수 in ["가", "나", "다", "라"]:
    print(변수)
#4번 호출됩니다. 기본적으로 for 문은 자료구조의 개수 만큼 코드를 반복 실행 합니다.
