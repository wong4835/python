#-*- coding:utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
for 변수 in ["사과", "귤", "수박"]:
    print(변수)
print("--")
#들여쓰기가 된 코드만 for문에 영향을 받기 때문에 for문의 실행이 모두 끝나고 "–"
#문자열이 화면에 출력됩니다.
