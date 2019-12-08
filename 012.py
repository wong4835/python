#-*- coding:utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
s = "hello"
t = "python"
print (s + '!' + t)
#s는 '1'이라고 보고 t는 '2'이라고 보면 s + '!' + t는 '1' +  '!' + '2'이므로 결과는
#hello!python 이라고 나온다. 만일 s가 김이고 t가 태웅이면 결과는 김태웅이 나온다.
