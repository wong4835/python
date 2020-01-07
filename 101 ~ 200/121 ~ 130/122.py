#-*- coding:utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
for 변수 in ["사과", "귤", "수박"]:
    print(변수)

#자료구조에는 세 개의 데이터가 있으므로 for문 안의 print 코드는 세 번 실행 됩니다.
#첫번째 : 변수에는 사과가 바인딩 됩니다. 이어서 print 코드가 실행되어 화면에 사과
#가 출력됩니다. 두번째 : 변수에는 귤이 바인딩 됩니다. 화면에 귤이 출력됩니다.
#* 세번째 : 변수에는 수박이 바인딩됩니다. 화면에 수박이 출력됩니다.
