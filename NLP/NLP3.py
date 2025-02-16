# -*- coding: utf-8 -*- 
from this import d
import nltk
nltk.download('punkt')
nltk.download('wordnet')

from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ############################### jaccard_similarity###################
def jaccard_similarity(d1, d2):
  lemmatizer = WordNetLemmatizer()
    
  words1 = [lemmatizer.lemmatize(word.lower()) for word in word_tokenize(d1)]
  words2 = [lemmatizer.lemmatize(word.lower()) for word in word_tokenize(d2)]

  inter = len(set(words1).intersection(set(words2)))
  union = len(set(words1).union(set(words2)))
  
  return inter/union

d1 = "Think like a man of action and act like man of though."
d2 = "Try no to become a man of success but rather try to become a man of value."
d3 = "Give me liberty, of give me death"


# # print(jaccard_similarity(d1, d2))
# # print(jaccard_similarity(d1, d3))
# # print(jaccard_similarity(d2, d3))

# # 0.2222222222222222
# # 0.06666666666666667
# # 0.058823529411764705

tiv = TfidfVectorizer()
corpus = [d1, d2, d3]

tfidf = tiv.fit_transform(corpus).todense()

# print(cosine_similarity(tfidf[0], tfidf[1]))
# print(cosine_similarity(tfidf[0], tfidf[2]))
# print(cosine_similarity(tfidf[1], tfidf[2]))

# [[0.22861951]]
# [[0.06083323]]
# [[0.04765587]]

import urllib.request

raw = urllib.request.urlopen('https://raw.githubusercontent.com/e9t/nsmc/master/ratings.txt').readlines()
# print(raw[:5])
# [b'id\tdocument\tlabel\n', 
# b'8112052\t\xec\x96\xb4\xeb\xa6\xb4\xeb\x95\x8c\xeb\xb3\xb4\xea\xb3\xa0 
# \xec\xa7\x80\xea\xb8\x88\xeb\x8b\xa4\xec\x8b\x9c\xeb\xb4\x90\xeb\x8f\x84 
# \xec\x9e\xac\xeb\xb0\x8c\xec\x96\xb4\xec\x9a\x94\xe3\x85\x8b\xe3\x85\x8b\t1\n',
# b'8132799\t\xeb\x94\x94\xec\x9e\x90\xec\x9d\xb8\xec\x9d\x84 \xeb\xb0\xb0\xec\x9a\xb0\xeb\x8a\x94
# \xed\x95\x99\xec\x83\x9d\xec\x9c\xbc\xeb\xa1\x9c, \xec\x99\xb8\xea\xb5\xad\xeb\x94\x94\xec\x9e\x90\xec\x9d\xb4\xeb\x84\x88\xec\x99\x80 
# \xea\xb7\xb8\xeb\x93\xa4\xec\x9d\xb4 \xec\x9d\xbc\xea\xb5\xb0 \xec\xa0\x84\xed\x86\xb5\xec\x9d\x84 \xed\x86\xb5\xed\x95\xb4 
# \xeb\xb0\x9c\xec\xa0\x84\xed\x95\xb4\xea\xb0\x80\xeb\x8a\x94 \xeb\xac\xb8\xed\x99\x94\xec\x82\xb0\xec\x97\x85\xec\x9d\xb4 
# \xeb\xb6\x80\xeb\x9f\xac\xec\x9b\xa0\xeb\x8a\x94\xeb\x8d\xb0. \xec\x82\xac\xec\x8b\xa4 \xec\x9a\xb0\xeb\xa6\xac\xeb\x82\x98\xeb\x9d\xbc\xec\x97\x90\xec\x84\x9c\xeb\x8f\x84 
# \xea\xb7\xb8 \xec\x96\xb4\xeb\xa0\xa4\xec\x9a\xb4\xec\x8b\x9c\xec\xa0\x88\xec\x97\x90 \xeb\x81\x9d\xea\xb9\x8c\xec\xa7\x80 \xec\x97\xb4\xec\xa0\x95\xec\x9d\x84 \xec\xa7\x80\xed\x82\xa8 
# \xeb\x85\xb8\xeb\x9d\xbc\xeb\x85\xb8 \xea\xb0\x99\xec\x9d\x80 \xec\xa0\x84\xed\x86\xb5\xec\x9d\xb4\xec\x9e\x88\xec\x96\xb4 \xec\xa0\x80\xec\x99\x80 \xea\xb0\x99\xec\x9d\x80 
# \xec\x82\xac\xeb\x9e\x8c\xeb\x93\xa4\xec\x9d\xb4 \xea\xbf\x88\xec\x9d\x84 \xea\xbe\xb8\xea\xb3\xa0 \xec\x9d\xb4\xeb\xa4\x84\xeb\x82\x98\xea\xb0\x88 \xec\x88\x98
# \xec\x9e\x88\xeb\x8b\xa4\xeb\x8a\x94 \xea\xb2\x83\xec\x97\x90 \xea\xb0\x90\xec\x82\xac\xed\x95\xa9\xeb\x8b\x88\xeb\x8b\xa4.\t1\n', 
# b'4655635\t\xed\x8f\xb4\xeb\xa6\xac\xec\x8a\xa4\xec\x8a\xa4\xed\x86\xa0\xeb\xa6\xac \xec\x8b\x9c\xeb\xa6\xac\xec\xa6\x88\xeb\x8a\x94 1\xeb\xb6\x80\xed\x84\xb0 
# \xeb\x89\xb4\xea\xb9\x8c\xec\xa7\x80 \xeb\xb2\x84\xeb\xa6\xb4\xea\xbb\x98 \xed\x95\x98\xeb\x82\x98\xeb\x8f\x84 \xec\x97\x86\xec\x9d\x8c.. \xec\xb5\x9c\xea\xb3\xa0.\t1\n', 
# b'9251303\t\xec\x99\x80.. \xec\x97\xb0\xea\xb8\xb0\xea\xb0\x80 \xec\xa7\x84\xec\xa7\x9c \xea\xb0\x9c\xec\xa9\x94\xea\xb5\xac\xeb\x82\x98.. 
# \xec\xa7\x80\xeb\xa3\xa8\xed\x95\xa0\xea\xb1\xb0\xeb\x9d\xbc\xea\xb3\xa0 \xec\x83\x9d\xea\xb0\x81\xed\x96\x88\xeb\x8a\x94\xeb\x8d\xb0 
# \xeb\xaa\xb0\xec\x9e\x85\xed\x95\xb4\xec\x84\x9c \xeb\xb4\xa4\xeb\x8b\xa4.. \xea\xb7\xb8\xeb\x9e\x98 \xec\x9d\xb4\xeb\x9f\xb0\xea\xb2\x8c \xec\xa7\x84\xec\xa7\x9c 
# \xec\x98\x81\xed\x99\x94\xec\xa7\x80\t1\n']

raw = [x.decode() for x in raw[1:10000]]

reviews = []
for i in raw:
    reviews.append(i.split('\t')[1])
    
# print(reviews[:5])

# ['어릴때보고 지금다시봐도 재밌어요ㅋㅋ', '디자인을 배우는 학생으로, 외국디자이너와 그들이 일군 전통을 통해 발전해가는 문화산업이 부러웠는데. 사실 우리나라에서도 그 어려운시절에 끝까지 열정을 지킨 노라
# 노 같은 전통이있어 저와 같은 사람들이 꿈을 꾸고 이뤄나갈 수 있다는 것에 감사합니다.', '폴리스스토리 시리즈는 1부터 뉴까지 버릴께 하나도 없음.. 최고.', '와.. 연기가 진짜 개쩔구나.. 지루할거라고 생각했 
# 는데 몰입해서 봤다.. 그래 이런게 진짜 영화지', '안개 자욱한 밤하늘에 떠 있는 초승달 같은 영화.']

from konlpy.tag import Mecab

tagger = Mecab('C:\mecab\mecab-ko-dic')

reviews = [tagger.morphs(x) for x in reviews]

# print(reviews)

# [['어릴', '때', '보', '고', '지금', '다시', '봐도', '재밌', '어요', 'ㅋㅋ'], ['디자인', '을', '배우', '는', '학생', '으로', ',', '외국', '디자이너', '와', '그', '들', '이', '일군', '전통', '을', '통해
# ', '발전', '해', '가', '는', '문화', '산업', '이', '부러웠', '는데', '.', '사실', '우리', '나라', '에서', '도', '그', '어려운', '시절', '에', '끝', '까지', '열정', '을', '지킨', '노라노', '같', '은', 
# '전통', '이', '있', '어', '저', '와', '같', '은', '사람', '들', '이', '꿈', '을', '꾸', '고', '이뤄나갈', '수', '있', '다는', '것', '에', '감사', '합니다', '.'], ['폴리스', '스토리', '시리즈', '는', '1', '부터', '뉴', '까지', '버릴', '께', '하나', '도', '없', '음', '.', '.', '최고', '.'], ['와', '.', '.', '연기', '가', '진짜', '개', '쩔', '구나', '.', '.', '지루', '할거', '라고', '생각', '했', '는
# 데', '몰입', '해서', '봤', '다', '.', '.', '그래', '이런', '게', '진짜', '영화', '지'], ['안개', '자욱', '한', '밤하늘', '에', '떠', '있', '는', '초승달', '같', '은', '영화', '.'], ['사랑', '을', '해', '본', '사람', '이', '라면', '처음', '부터', '끝', '까지', '웃', '을', '수', '있', '는', '영화'], ['완전', '감동', '입니다', '다시', '봐도', '감동'], ['개', '들', '의', '전쟁', '2', '나오', '나요', '?', '나오', '면', '1', '빠', '로', '보', '고', '싶', '음'], ['굿'], ['바보', '가', '아니', '라', '병', '쉰', '인', '듯'], ['내', '나이', '와', '같', '은', '영화', '를', '지금', '본', '나', '는', '감동
# ', '적', '이', '다', '.', '.', '하지만', '훗날', '다시', '보면대', '사', '하나', '하나', '그', '감정', '을', '완벽', '하', '게', '이해', '할', '것', '만', '같', '다', '.', '..'], ['재밌', '다'], ['고 
# 질라', '니무', '귀엽', '다', '능', 'ㅋㅋ'], ['영화', '의', '오페라', '화', '라고', '해야', '할', '작품', '.', '극단', '적', '평갈', '림', '은', '어쩔', '수', '없', '는', '듯', '.'], ['3', '도', '반전', '좋', '았', '제', '^^'], ['평점', '왜', '낮', '아', '?', '긴장감', '스릴감', '진짜', '최고', '인데', '진짜', '전장', '에서', '느끼', '는', '공포', '를', '생생', '하', '게', '전해', '준다', '.'], [' 
# 네', '고시', '에', '이터', '랑', '소재', '만', '같', '을', '뿐', '.', '.', '아무런', '관련', '없', '음', '.', '.'], ['단연', '최고'], ['가', '면', '갈수록', '더욱', '빠져드', '네요', '밀회', '화이팅', '!', '!'], ['어', '?', '생각없이', '봤', '는데', '상당', '한', '수작', '.', '일본', '영화', '10', '년', '내', '최고', '로', '마음', '에', '들', '었', '다', '.', '강렬', '한', '임팩트', '가', '일품', 
# '.'], ['오랜만', '에', '본', '제대로', '된', '범죄', '스릴러', '~'], ['그런', '때', '가', '있', '었', '다', '.', '(', "'", '사랑', '해', "'", '도', '아니', '고', ')', '그저', '좋', '아', '한다는', '한
# ', '마디', '말', '을', '꺼내', '기', '도', '벅차', '서', '밤', '잠', '설치', '던', '때', '.', '커', '징', '텅', '의', '교복', '에', '남', '은', '션', '자이', '의', '볼펜', '자국', '역시', '미처', '다', '전하', '지', '못한', '마음', '의', '형태', '인', '거', '다', '.'], ['마지막', '씬', '을', '잊', '을', '수', '가', '없', '다'], ['강압', '적', '용서', ',', '세', '뇌', '적', '용서', '에', '대한', ' 
# 비판'], ['중세', '시대', '명작', '.', '굿', '평점', '이', '왜', '이래'], ['7', '시간', '짜리', '영상', '이', '존재', '한다면', ',', '죽', '기', '전', '에', '꼭', '한번', '보', '고', '싶', '다', '.', '아름답', '고', '슬픈', 'OST', ',', '제니퍼코넬리', '의', '눈부신', '아역', '시절', ',', '로버트드니로', '의', '마지막', '웃', '는', '장면', '까지', '정말', '가슴', '속', '에', '영원히', '기억', '될', 
# '최고', '의', '명작', '이', '다', '.'], ['사람', '이', '어떻', '게', '저런', '짓', '을', '할', '수', '가', '있', '는지', 'ㅡㅡ', '보', '는', '내', '가', '다', '화나', '더라'], ['인간', '의', '잠재', '된', '악마', '성', '은', '여러', '시간', '과', '공간', '속', '에서', '존속', '해', '왔', '다', '.', '이', '다큐', '는', '그것', '을', '엉뚱', '하', '면서', '도', '광적', '으로', '재현', '하', '였', ' 
# 다', '.'], ['최고', '다', '.', '삼', '일', '동안', '쉬', '는', '틈틈이', '잠', '도', '줄여', '가', '면서', '봤', '다', '.', '.', '여운', '이', '남', '는다', '.'], ['실화', '여서', '더욱', '충격', ',', '다시', '는', '어디', '에서', '도', '일어나', '서', '는', '안', '될', '경각심', '을', '일깨워', '주', '는', '영화'], ['존', '그라', '샴', '작품', '이', '라면', '한', '번', '쯤', '은', '볼', '가치', '가', '있', '지'], ['농아', '인', '문화', '에', '대한', '알', '아야', '합니다', '.'], ['이거', '어렸', '을', '때', '되게', '재밌', '게', '봄', 'ㅋㅋ', '이정재', '이범수', 'ㅋㅋ', 'ㅋㅋ', '연기', '쩜'], ['친구', '의', '우정', '이', '매우', '감동', '적', '이', '었', '다'], ['굿', '굿', '굿', '또', '해라', '또', '해라', '제발', 'ㅠㅠ'], ['아', '재미있', '다', '.', '이', '말', '이', '너무', '어울린다', '.'], ['제이크', '질렌할', '.', '.', '넌', '대체', '못', '하', '는', '연기', '가', '뭐', '냐', '.'], ['보', '는', '내내', '입가', '에', '미소', '가', '샤', '방', '샤', '방', '했', '던', '영화', '.'], ['원표', '가', '왜', '조연', '이양', '.', '..', '젤', '많이', '나오', '는구만', '.', '..', 'ㅋㅋ', '재미', '있', '음', '.', '..'], ['마치', '바다', '속', ',', '아쿠아리움', '속', '으로', '들어간', ' 
# 듯', '한', '느낌', '의', '영화', '어린', '자녀', '들', '에게', '강추', '!', '!'], ['정의', '를', '세우', '는', '콜트', ',', '콜', '텍', '노동자', '들', '이야기'], ['이', '영화', '보', '면', '브라질', 
# '가', '고', '싶', '은', '마음', '이', '사라질', '것', '이', '다', '.'], ['난', '남자', '지만', '영화', '내내', '마음', '이', '울렸', '다', '그리고', '내', '가', '좋', '아', '하', '는', '두', '여배우', '!', '!'], ['도법', '멤버', '들', '모두', '기대', '됨'], ['정말', '재미있', '게', '본', '영화', '였', '다', '액션', '최고'], ['내', '가', '남자', '라', '그런가', '이거', '겁나', '긴장감', '있', '고', '흥미진진', '하', '던데', '.', '.', 'ㄷ', 'ㄷ', '나', '만', '그런가', '워낙에', '격투', '씬', '을', '좋아해서', '.', 'ㅋㅋㅋ', '그냥', '아무', '생각', '없이', '집', '에서', '스마트', '티비', '로', ' 
# 봐서', '재밌', '었', '나', '봄', '이거', '뭔', '영화', '인지', '도', '모르', '고', '암살', '에', '나온', '이정재', '있', '길래', '걍봄', 'ㅋㅋ', '하여튼', '너무', '재밌', '게', '봤', '음'], ['인정', '할', '건', '인정', '하', '자', 'ㅆ파르', '년', '들', '아', '북한', '이', '살만', '하', '고', '좋', '으면', '왜', '목숨걸', '고', '대한민국', '오', '는', '건데', '어', '?', '그거', '부터', '납득', '시 
# 키', '고', '나불거려', '라', '종북', '박평식', '같', '은', '좋', '가', '튼', '년', '들', '아'], ['잊', '을', '수', '없', '는', '그대', '여', ',', '6', '월', '이', '되', '고', '비', '가', '내려야', '그
# 대', '가', '보이', '기', '시작', '합니다', '.'], ['반가운', '얼굴', '들', '~', 'ㅋㅋㅋ', '여주인공', '넘', '매력', '적', '이', '구', '~', '유쾌', '한', '영화', '였', '어요', '~~'], ['내용', '이', '너 
# 무', '좋', '아요', '.', 'ㅎ'], ['정말', '요즘', '아이', '돌', '들', '이', '다', '배우', '해', '먹', '네', '할', '정도', '로', '연기', '를', '잘', '한다'], ['정말', '재', '밋', '게', '봣는대요', '어디', '서', '받', '을', '수', '잇', '조', '?'], ['탱고', '음악', '의', '감동', '이', '밀려온다', '.'], ['평생', '못', '봤', '으면', '후회', '할', '뻔', '한', '따뜻', '한', '명작'], ['이런', '드라마', '가', '많이', '나왔', '으면', '좋', '겠', '어요', '.', '생각', '할', '것', '도', '많', '고', '영상미', '도', '아름답', '고', '캐릭터', '도', '다', '매력', '있', '었', '어요', '.', '여러', '가지', '로', ' 
# 다', '매력', '있', '었', '던', '드라마', '였', '어요', '.'], ['정말', '최고', '였', '는데', '.', '.', '마지막', '이', '.', '.', '이', '련결', '말', '.', '싫', '다', '.', '.', 'ㅠ'], ['너무', '슬프', '네요', '.', '왜', '이제', '알', '게', '된', '영화', '였', '는지', '.'], ['잔잔', '하', '고', '재미', '도', '있', '어서', '좋', '았', '다'], ['내', '가', '본', '영화', '중', '영순위', '♥'], ['재밌', ' 
# 습니다', '.', '재밌', '습니다', '.'], ['상당히', '훌륭', '한', '영화', '.', '..'], ['역시', '신동엽', 'ㅋ', '순간', '캐치', '탁', '!', '얄밉', '게', '웃', '긴', '미워할', '수', '없', '고', '감탄', '!', '이영자', '랑', '함', '대박', '일', '텐데', '왠', '이동욱', '?'], ['내', '인생', '의', '영화'], ['전작', '에', '비해', '떨어지', '는', '건', '사실', '이', '지만', '쓰레기', '한국', '영화', '도', '4', '점', '대', '별로', '없', '는', '데', '헐', '.', '..', '니', '들', '너무', '하', '다', '?'], ['지금', '은', '다소', '진부', '할', '수', '있', '어도', '그', '당시', '엔', '눈물', '한', '사발', '흘리', '게', '해', '준', '영화', '.'], ['신부', '로서', '의', '사명감', '을', '처절히', '실천', '하', '는', '제리', ',', '자신', '마저', '부정', '하', '는', '로키', '의', '우정'], ['3', '.', '14', '원주율', '메이커'], ['추석', '때', '특선', '영화', '해', '주', '는', '거', '봤', '는데', '진짜', '가족', '들', '끼리', '보', '기', '좋', '은', '영화', '였', '음', '!'], ['"', '우리', '애기', '첫', '영화', ' 
# 너무너무', '잘', '선택', '한', '거', '같', '아요', '""""', 'ㅎ', '굳', '"'], ['재미있', '어요'], ['생각', '보다', '괜찬은조합인거같다'], ['저게', '바로', '이', '시대', '의', '어머니', '.'], ['나', '만
# ', '재밌', '으면', '되', '지', '뭐', '나', '도', '원작', '본', '사람', '이', '지만', '드래곤볼', '에볼루션', '보다', '는', '잘', '만', '듬', 'ㅇㅇ'], ['우리', '나라', '예능', '중', '최고', '!', '!'], 
# ['방학', '때', '아침', '에', '졸린', '눈', '비비', '면서', '우연히', '티비', '채널', '돌리', '다', '이', '영화', '를', '보', '게', '된', '건', '정말', '.', '.'], ['마음', '이', '너무', '아프', '다', '.', '이', '영화', '는', '다시', '볼', '수', '없', '을', '것', '같', '다', '.'], ['엔', '트랩', '먼', '트'], ['정말', '재미있', '게', '보', '았', '음', '.', '권력', '에', '는', '친구', '도', '의리', ' 
# 도', '없', '다는', '역사', '적', '사실', '을', '훌륭', '하', '게', '깨우쳐', '줌', '.'], ['처음', '에', '는', '초롱', '팬', '심', '으로', '봤', '는데', '갈수록', '내용', '과', '어울리', '는', '배경', 
# '음악', '들', '이', '너무', '달달', '하', '고', '보', '고', '있', '으면', '행복', '해', '지', '네요', '.', '완전', '재밌', '습니다', '.'], ['너무너무', '재밌', '게', '보', '고', '있', '어요', '!', '중
# 간', '부터', '본방', '사수', '했', '지만', '스토리', '가', '탄탄', '하', '고', '흥미진진', '해서', '1', '화', '부터', '다', '찾', '아서', '봤', '네요', '배우', '들', '연기', '도', '어디', '하나', '빠 
# 지', '는', '데', '가', '없', '네요', '요새', '는', '수백', '향', '만', '챙겨', '봐요'], ['내', '가', '없', '어질', '내', '인생', '.', '제목', '을', '참', '잘', '지', '었', '다', '.'], ['음', '화질', '은', '좋', '은데', '재미', '가', '없', '네'], ['가을', '로', '는', '가을', '에', '감동', '이', '네요'], ['ost', '때문', '에', '봤', '는데', '이건', '뭐', '와', '~~', '라는', '말', '밖에', '안', '나오', '네', '벌써', '16', '년', '전', '인데', '이런', '퀄리티', '가', '나오', '다니', '대단', '하', '다'], ['중', '3', '인데', '일단', '2', '까지', '봣다', '.', '뭐', '말', '할', '것', '도', '없', '다', '장국영', '자살', '이', '안타깝', '다'], ['사실', '적', '이', '어서', '더', '극', '적', '인', '.'], ['뀰잼이다뀰잼이라구여'], ['짱', '재미있', '어', '요오', '>', 'ㅇ', '<'], ['첫', '느낌', '은', '예전', '에', '양심', '냉장고', '와', '비슷', '한', '거', '같', '더라고요', '보', '면서', '감정', '이', '움찔', '해', '져요', '그런대', '한', '가지', '부탁', '드리', '고', '싶', '은', '게', '연기자', '좀', 
# '보호', '해', '주', '세요', '욕', '이나', '폭력', '은', '걱정', '되', '요', '저', '어릴', '적', '에', '성추행', '을', '상가', '에서', '모든', '사람', '이', '목격', '했', '는데', '저', '만', '증언', ' 
# 했었', '거든요', '덕분', '에', '청소년', '인', '저', '는', '계속', '경찰서', '를', '왔', '다', '갔', '다', '해야', '했', '죠'], ['남자', '주인공', '넘', '섹시', '하', '고', '멋있', '쪙ㅋㅋㅋㅋ'], ['어
# 설픈', '건', '사실', '이', '었', '다', '하', '지', '재', '밋', '었', '다', 'ㅎ'], ['SF', '영화', '중', '21', '세기', '최고', '라고', '할', '수', '있', '다', '.', '.', '이걸', '평점', '낮', '게', '주', '는', '사람', '은', '정말', '볼', '줄', '을', '모르', '는', '것'], ['95', '년', '에', '비디오', '방', '에서', '친구', '랑', '봤', '는데', '정말', '좋', '았', '다는', '느낌', '이', '지금', '까지', '.', '..', '또', '보', '고', '싶', '네요'], ['빨리', '보', '고', '싶', '다', '!', '!!', '헌데', '오래', '기다려야', '될', '거', '가', '틈', '.', '..'], ['남기남', '감독', '그', '이름', '하나', '만', '으 
# 로', '도', '10', '점'], ['진짜', '최고', '다', '최고', '성룡', '형', '님', '마이', '우상'], ['amy', '6250', '당신', '이', '좋', '아', '하', '는', '장르', '는', '뭐요', '?', '이', '영화', '에', '도', '저', '영화', '에', '도', '이런', '장르', '는', '싫', '다', '니원'], ['지금', '까지', '본', '영화', '중', '에', '최고', '다'], ['매회', '리타', '가', '자꾸', '거슬려서', '죽', '었', '으면', '좋', '겠', '다고', '생각', '했', '는데', 'ㅠㅠ죄책감에나도잠못이룬다', '.'], ['어릴', '때', '보', '고', '커서', '다시', '봤', '는데', '.', '진짜', '잘', '만든', '영화', '였', '네', '.', '웃음', '과', '감동', ' 
# 을', '잘', '이어', '붙였', '고', '정치', '에', '대한', '비판', '이랑', '묘사', '도', '굉장히', '잘', '표현', '했', '다', '.', '흥', '행했었', '는지', '기억', '은', '안', '나', '지만', '절대', '낮', ' 
# 은', '평점', '의', '영화', '가', '아니', '라고', '생각', '한다', '.', '연기자', '들', '연기', '하', '는', '디테일', '만', '봐도', '따', '봉', '임'], ['대박', '이', '였', '지', '이건', '한마디', '로', 
# '.', '.'], ['사랑', '은', '달', '기', '만', '한', '게', '아니', '라는', '거', '.'], ['마음', '을', '파', '고', '든다', '.', '...', '볼', '수록', '빠져드', '는', '영화', '.', '.'], ['13', '살', '이', '엇', '냐', '?', '...'], ['남자', '얼굴', '성격', '10', '점', '만점', '에', '10000', '점'], ['잼', '있', '어요', '!', '다음', '에', 'ㄸㅗ', '보', '고', '싶', '어요'], ['핡'], ['초반', '엔', '황당', '한
# ', '설정', '이', '다', '싶', '어', '몰입', '이', '힘들', '었', '지만', '점차', '이건', '판타지', '가', '아니', '라', '우리', '의', '근', '미래', '에', '현실', '이', '될지', '도', '모르', '는', '언론', '탄압', '에', '대한', '진지', '한', '은유', '라는', '생각', '이', '들', '었', '다', '.', '남자', '주인공', '오카다', '준이치', '는', '예상', '보다', '훨씬', '좋', '았', '다', '.', '별', '기대', '없이
# ', '보', '았', '는데', '의외', '의', '재미', '와', '감동', '.'], ['인도', '영화', '는', '역시', '!', '!!', '스토리', ',', '영상', ',', '배우', '들', '의', '연기', '까지', '뭐', '하나', '빠지', '는', '거', '없이', '꽉', '찬', '영화', '!', '!', '대박', '감동', '~', 'ㅠㅠ'], ['순수', '함', '그리고', '진짜', '웃음', '이', '무엇', '인지', '알', '수', '있', '었', '다', '그', '가', '웃', '을', '때', '나', '도', '모르', '게', '웃', '게', '되', '는', '순수', '함'], ['좀', '짱', '인', '듯', '허정무', '대신', '장외룡', '감독', '을', '한국', '국', '대로', '고고', '싱'], ['ㅎㅎㅎ', 'ㅎㅎㅎ', 'ㅎㅎ'], ['어 
# 찌', '그런', '사명감', '을', '가질', '수', '있', '단', '말', '인가', '.'], ['정말', '행복', '했', '다', '.', '..', '계속', '미소', '지으', '면서', '봐서', '보조개', '가', '아프', '네', 'ㅎㅎ'], ['와', '~', '정말', '재밌', '네요', '!', '!'], ['에니', '메이', '션', '최', '고봉', '중', '하나', '초딩', '때', '진짜', '잼', '나', '게', '봣음', 'ㅋㅋㅋ'], ['비포', '미드나잇', '을', '마지막', '으로', '그', '들', '을', '떠나보내', '는', '내', '심정', '또한', '아련', '하', '지만', '한편', '으로', '는', '행복', '하', '게', '지내', '는', '그', '들', '의', '모습', '을', '보', '니', '절로', '웃음', '이', ' 
# 지', '어', '진다'], ['재미', '는', '없', '지만', '뭔가', '가', '있', '다', '.'], ['코스케', '가', '라디오', '에서', '임진강', '을', '부를', '때', '는', '눈물', '이', '멈추', '지', '않', '았', '다'], ['한석규', '연기', '짱', 'ㅎㅎㅎ', '~~~'], ['쵝오'], ['진짜', '허니', '잼', '꿀', '잼', '개꿀', '잼', '꼭', '보', '셈'], ['한예슬', '진짜', '너무', '이', '쁘당ㅋㅋㅋ짱인듯원래도', '이쁜데', '미탄', '에
# 서', '이', '쁨터짐ㅋㅋㅋ옷입는것도', '헤어', '도', '메이크업', '도', '이쁨', '이', '쁨이쁨드라마', '내용', '도', '괜찮', '고', '잘', '될', '듯', 'ㅋㅋㅋ'], ['딱', '한', '마디', '만', '하', '겠', '습니
# 다', '.', '......', '최고', '!', '!!'], ['재미', '반', '기대', '반', '이', '네요', 'ㅎㅎ', '더욱', '기대', '합니다'], ['정말', '정말', '정말', '명작', '입니다', '.', 'ㅠ', '_', 'ㅠ', '우연히', '봤', '는데', '정말', '빠져', '들', '었', '어요', '!'], ['완전', '잼', '있', '네요', '훈', '남', '쉐프', '님', '들', '도', '보', '구', '요리', '도', '배우', '고', '^♥^'], ['좋', '은', '시나리오', ',', '비고', '모르텐슨', '의', '좋', '은', '연기', '.'], ['잼', '잼', '꿀', '잼', '허', '니', '잼', '핵', '잼', '잼', '잼'], ['개인', '적', '으로', '재미있', '었', '습니다', '.', '언제', '팬텀', '이랑', '크리스 
# 틴', '이랑', '그런', '일', '이', '있', '었', '는지', '전혀', '몰랐', '네요', '.', '...', 'ㅠㅠㅠ', '일반', '스토리', '들', '처럼', '크리스틴', '이', '다시', '남편', '곁', '으로', '돌아갔었', '더라면', '하', '는', '아쉬움', '은', '있', '네요', 'The', 'Beauty', 'Underneath', '가', '젤', '좋', '았', '어요', '개인', '적', '으로', 'ㅋㅋㅋ'], ['알파치노', '연기', '때문', '에'], ['이', '영화', '는', '처 
# 음', '과', '끝', '에서', '명화', '로', '다시', '태어났', '다', '.'], ['뮤지컬', '역대', '1', '위', '가', '괜히', '된', '게', '아니', '었', '군요', '.', '이건', '정말', '이', '지', '대부', ',', '바람', '과', '함께', '사라지', '다', '레벨', '의', '영화', '입니다', '.', '3', '명', '의', '주인공', '은', '마치', '뮤지컬', '계', '의', '마', '잭', ',', '마돈나', ',', '엘비스', '급', '의', '춤', '과', '노
# 래', '실력', '을', '보여줌', '.'], ['바비도', '잘', '했', '고', '바스코', '도', '잘', '했', '다', '.', '이번', '결과', '에', '대해서', '불만', '을', '품', '는', '사람', '들', '이', '나오', '는', '건', '어쩌면', '당연', '한', '거', '지만', ',', '그래도', '바비', '를', '아이돌', '이', '네', '어', '쩌', '네', '하', '고', '깎아내리', '면서', '까지', '까', '는', '건', '아니', '라고', '본다', '.', '바비
# ', '는', '충분히', '이길', '자격', '이', '있', '었', '다고', '개인', '적', '으로', '생각', '한다', '.'], ['코미디', '사극', '에', '장혁', '의', '명품', '연기', '까지', '.', '..'], ['어릴', '땐', '온', '가족', '이', '서', '봤', '던', '영화', '.', '처음', '으로', '집', '마련', '하', '고', '이사', '마치', '고', '그날', '저녁', '에', '본', '영화', '.', '그', '때', '의', '기분', '탓', '인진', '몰랐', '는지', '만', '그렇게', '웃길', '수', '가', '없', '었', '다', '.'], ['옛날', '에', '워낭', '소리', '봤', '을', '때', '진짜', '많이', '울', '었', '는데'], ['내', '인생', '최고', '의', '명작', '입니다'], ['재밌', '나요', '?', '더', '빙', '을', '보', '는데', 'ㅠ자막이더좋긴한데'], ['5', '년', '뒤', '에', '찾아봐도', '아련', '하', '겠', '지', "'", '포', "'", '씨', '처럼'], ['연말', '에', '추천', '할', 
# '만', '한', '따뜻', '한', '영화', '.', '배경', '음악', '도', '참', '좋', '았', '다'], ['한국', '사회', '의', '치부', '를', '정확', '하', '게', '예언', '한', '수작'], ['제', '가', '좋', '아', '하', '는
# ', '영화', '중', '진짜', '찐', '짜', '좋', '아', '하', '는', '영화', '.', '..', ':', ')'], ['지금', '은', '아니', '지만', '엣', '날', '에', '내', '가', '제일', '좋', '아', '했', '던', '영화'], ['역시', '최고', '였', '다', '.'], ['슈퍼', '울트라', '초', '재밌', '음', '.', '노', '막', '입', '벌릴', '때', '참', '매력', '있', '음', 'ㅋ'], ['중동', '의', '문화', '에', '대해서', '새롭', '게', '알', '게', '한', '영화'], ['11', '명', '참여', '라길래', '얼마나', '바뀌', '나', '궁금', '해서', '올려', '봄'], ['좀', '지루', '하', '긴', '했', '지만', '아버지', '이', '자', '남편', ',', '무사', '로서', '의', '한', '남자', '의', '일생', '을', '잘', '보여줌', '의미', '없', '는', '죽음', '일지', '도', '모르', '겠', '지만', '자신', '의', '굳', '은', '신념', '이', '있', '다는', '건', '참', '멋진', '일', '이', '다', '.'], ['웃음', '과', '감동', '의', '물결', '기대', '안', '하', '고', '봤', '는데', '쵝오임'], ['좋', '은', '영화', '.', '다만', '엔딩', '에서', '주인공', '이', '배심원', '들', '을', '상대', '로
# ', '늘어놓', '는', '일장', '연설', '이', '너무', '작위', '적', '이', '고', '신', '파조', '.', '이', '연설', '에', '흔들려서', '배심원', '들', '이', '무죄', '로', '돌아선다는', '것', '도', '너무', '억 
# 지', '스럽', '고', '.', '해�

from gensim.models import Word2Vec
from sklearn.manifold import TSNE
from matplotlib import font_manager as fm 
from matplotlib import rc


Word2Vec = Word2Vec(reviews, min_count=5)
print(Word2Vec) #Word2Vec(vocab=2639, size=100, alpha=0.025)

# print(Word2Vec.wv.most_similar('영화'))

# [('작품', 0.9590977430343628), ('듯', 0.9588232040405273), ('이야기', 0.9518460035324097), ('마음', 0.9498653411865234),
#  ('따뜻', 0.9454899430274963), ('에게', 0.9446271657943726), ('표현', 0.9406832456588745), ('모습', 0.9399892687797546), 
#  ('모든', 0.9379570484161377), ('일깨워', 0.937619149684906)]

tsne = TSNE(n_components=2)

vocab = Word2Vec.wv.vocab
similarity = Word2Vec[vocab]

# print(similarity)
# [[-1.9043018e-01  6.0458086e-02  3.0009714e-01 ... -1.8012035e-01
#    6.3681245e-02  7.4641250e-02]
#  [-3.4279200e-01  2.1309337e-01  5.9416842e-01 ... -3.5661131e-01
#    1.5126483e-01  3.5050571e-01]
#  [-3.7055114e-01  7.9309529e-01  1.1108963e+00 ... -2.3339659e-01
#    5.1982224e-01 -4.4668660e-01]
#  ...
#  [-2.5556203e-02  4.4172769e-03  3.4531422e-02 ... -3.1892009e-02
#    2.3240244e-03  8.3151609e-03]
#  [-2.4718102e-02 -5.8258194e-03  3.5480313e-02 ... -3.0980976e-02
#    3.5981418e-04  1.1760187e-02]
#  [-3.2516293e-02  8.5264649e-03  5.6635175e-02 ... -3.7112448e-02
#    3.3254067e-03  1.8833291e-02]]

import pandas as pd 
transform_similarity =tsne.fit_transform(similarity)
df = pd.DataFrame(transform_similarity, index=vocab, columns=['x', 'y'])
# print(df[0:10])

#             x          y
# 어릴 -19.199011 -14.274330
# 때   15.692836 -65.422470
# 보   13.439113 -68.261230
# 고   13.949283 -66.928116
# 지금  11.611351 -65.688393
# 다시  12.516029 -66.905235
# 봐도   7.467353 -68.248573
# 재밌   3.173648 -70.451248
# 어요   2.661175 -68.920540
# ㅋㅋ  -0.196866 -69.428802

import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')

# sns.lmplot('x','y', data=df, fit_reg=False, size=8)
# plt.show()

from sklearn.cluster import AgglomerativeClustering, k_means

# ward = AgglomerativeClustering(n_clusters=6, linkage='ward')
# predict =ward.fit_predict(df)
# print(predict)
# [3 5 5 ... 1 1 1]

# results =df
# results['predict'] = predict
# print(results[0:10])

#          x          y  predict
# 어릴 -21.083561  17.694132        3
# 때  -60.386024 -13.401434        1
# 보  -62.418568 -16.870384        1
# 고  -62.567547 -15.846326        1
# 지금 -60.299015  -9.980978        1
# 다시 -63.133499 -15.370501        1
# 봐도 -64.995453  -4.656458        1
# 재밌 -69.374550  -2.769756        1
# 어요 -68.269699  -2.189960        1
# ㅋㅋ -68.636497   0.450870        1

# sns.lmplot('x', 'y', data=results, fit_reg=False, size=8, hue="predict")
# plt.show()

# avg = AgglomerativeClustering(n_clusters=6, linkage='average')
# predict =avg.fit_predict(df)
# # print(predict)
# # [2 5 5 ... 4 4 4]

# results =df
# results['predict'] =predict
# print(results[0:10])

#             x          y  
# 어릴  27.309803   9.229890        2
# 때   50.252216 -30.312670        4
# 보   53.469326 -32.808594        4
# 고   52.289093 -32.929359        4
# 지금  52.329144 -29.474146        4
# 다시  53.271362 -31.464766        4
# 봐도  54.065277 -29.858133        4
# 재밌  63.566486 -24.896664        4
# 어요  62.213833 -24.776804        4
# ㅋㅋ  64.221390 -22.704771        4

# sns.lmplot('x','y', data=results, fit_reg=False, size=6, hue='predict')
# plt.show()

# compl = AgglomerativeClustering(n_clusters=6, linkage='complete')
# predict = compl.fit_predict(df)
# # print(predict)
# # [2 3 3 ... 4 4 4]

# results = df
# results['predict'] = predict
# print(results[0:10])

#             x          y  predict
# 어릴  -3.354240  24.470833        3
# 때  -53.373676  16.511683        2
# 보  -57.066380  10.382351        2
# 고  -56.058834  11.323556        2
# 지금 -53.782860  19.326752        2
# 다시 -54.933331  18.535915        2
# 봐도 -54.790867  20.541578        2
# 재밌 -58.343948  26.818649        2
# 어요 -57.050514  26.135355        2
# ㅋㅋ -56.431911  29.547745        2

# sns.lmplot('x', 'y', data=results, fit_reg=False, size=6, hue='predict')
# plt.show()

from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import linkage, dendrogram

distmatrix = pdist(df, metric ='euclidean')

row_dist = pd.DataFrame(squareform(distmatrix))
# print(row_dist)

#            0          1          2          3          4          5          6          7     ...        2631       2632       2633       2634       2635       2636       2637       2638
# 0      0.000000  50.961344  44.743811  46.525562  45.020986  45.549803  44.037368  44.928978  ...   51.288058  58.611246  51.679508  54.646965  47.887205  58.931459  60.204058  61.586994
# 1     50.961344   0.000000  10.098654   8.854635   8.701243   9.255019  16.440141  21.099264  ...  102.105176  84.900318  94.396755  71.773127  78.449256  75.670579  78.129292  84.463612
# 2     44.743811  10.098654   0.000000   1.831537   1.551225   0.943147   6.655590  11.577418  ...   95.142245  85.494015  91.550785  73.647596  77.954998  77.791333  80.121320  85.720450
# 3     46.525562   8.854635   1.831537   0.000000   1.882234   0.978376   7.587579  12.329309  ...   96.966102  86.596455  93.085886  74.544191  79.201028  78.653515  81.006637  86.725289
# 4     45.020986   8.701243   1.551225   1.882234   0.000000   1.174470   8.206610  13.127000  ...   95.624695  84.717131  91.283769  72.695646  77.320952  76.813215  79.160900  84.856845
# ...         ...        ...        ...        ...        ...        ...        ...        ...  ...         ...        ...        ...        ...        ...        ...        ...        ...
# 2634  54.646965  71.773127  73.647596  74.544191  72.695646  73.829329  77.861011  81.731164  ...   81.496377  16.053160  43.505507   0.000000  18.563709   4.437262   6.491313  13.327987
# 2635  47.887205  78.449256  77.954998  79.201028  77.320952  78.349872  80.851273  83.924125  ...   64.511896  11.244917  24.988807  18.563709   0.000000  20.178916  19.442750  15.748549
# 2636  58.931459  75.670579  77.791333  78.653515  76.813215  77.953333  82.100046  86.016355  ...   84.187494  14.972789  44.639609   4.437262  20.178916   0.000000   2.604814  10.923765
# 2637  60.204058  78.129292  80.121320  81.006637  79.160900  80.296833  84.352095  88.219759  ...   83.828487  12.977350  43.405337   6.491313  19.442750   2.604814   0.000000   8.506662
# 2638  61.586994  84.463612  85.720450  86.725289  84.856845  85.966564  89.540725  93.158369  ...   79.648998   5.615672  37.102539  13.327987  15.748549  10.923765   8.506662   0.000000

# [2639 rows x 2639 columns]

# row_clusters = linkage(distmatrix, method='complete')

# plt.figure(figsize=(20,10))
# dendrogram(row_clusters, leaf_rotation=50, leaf_font_size=7)
# plt.show()

# mergings = linkage(df,method='complete')

# plt.figure(figsize=(20,10))
# dendrogram(mergings, leaf_rotation = 50, leaf_font_size = 7)
# plt.show()

from sklearn.cluster import KMeans 

Kmeans = KMeans(n_clusters=3)
predict = Kmeans.fit_predict(df)
# print(predict)

# [0 0 0 ... 1 1 1]

results = df
# results['predict'] = predict
# print(results[0:10])

#            x          y  predict
# 어릴  13.421665  21.371149        1
# 때  -26.761028  53.625114        1
# 보  -27.465942  58.624767        1
# 고  -26.635664  59.035675        1
# 지금 -24.688776  57.788921        1
# 다시 -26.370430  58.455505        1
# 봐도 -24.378124  58.598560        1
# 재밌 -18.365118  64.925713        1
# 어요 -17.207811  64.220467        1
# ㅋㅋ -14.760289  65.818932        1

# sns.lmplot('x', 'y', data=results, fit_reg=False, size=6, hue='predict')
# plt.show()

kmeans = KMeans(n_clusters=6)
predict = kmeans.fit_predict(df)
# print(predict)
# [2 1 1 ... 3 3 3]

results = df
results['predict'] = predict
# print(results[0:10])

#             x          y  predict
# 어릴  27.724405   1.061452        3
# 때   19.871454 -52.827572        1
# 보   16.507990 -57.892410        1
# 고   18.147495 -57.492851        1
# 지금  20.372841 -55.102779        1
# 다시  19.034897 -56.631817        1
# 봐도  22.422367 -55.294930        1
# 재밌  29.249611 -56.130856        1
# 어요  28.441271 -54.785275        1
# ㅋㅋ  31.578482 -54.628864        1

# sns.lmplot('x','y', data=results, fit_reg=False, size=6, hue='predict')
# plt.show()



