from konlpy.tag import Okt #open korean text(트위터)  
okt = Okt()  
token = okt.morphs("나는 자연어 처리를 배운다")  
print(token)
