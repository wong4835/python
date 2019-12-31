t = (1, 2, 3)
t[0] = 'a'
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    t[0] = 'a'
TypeError: 'tuple' object does not support item assignment
#tuple은 element의 값을 변경할 수 없습니다.
