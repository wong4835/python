#-*- coding:utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

movie_rank=["닥터 스트레인지","스필릿","럭키"]
movie_rank.append("배트맨")
print(movie_rank)
#['닥터 스트레인지', '스플릿', '럭키', '배트맨']
