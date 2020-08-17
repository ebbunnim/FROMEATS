# 추천 시스템 구현 방법 = 협업필터링 + 내용기반

'''
[협업필터링]
 - 유저들의 취향 정보들을 기반으로 하여 스스로 예측하는 기술
 - A가 이슈에 대해 B와 같은 의견 -> 다른 이슈에대해서도 비슷한 의견 가질 것
 - Memory-based 협업 필터링 = 사용자기반, 아이템기반
    - ex.
           공조  더킹  라라랜드  컨택트  너의이름은
      재석	 5	  4	     4	       3	 
      명수	 1	  0	     1	 	            4
      하하	 4	  4	    		   5	    3
      준하	 	  2	     1	       4	    3
      세형	 4	 	     4	       4	    2
      광희	 4	  2	     3	 	            1 

    [1. 사용자 기반]
    - 명수와 준하의 유사도 -> 두 사용자가 공통으로 평가한 항목에대해서만 계산 -> A=(0, 1, 4), B=(2, 1, 3)
    - 유사도
            	재석	명수	 하하	 준하	 세형	 광희
        재석	1.00	0.84	0.96	0.82	0.98	0.98
        명수	0.84	1.00	0.61	0.84	0.63	0.47
        하하	0.96	0.61	1.00	0.97	0.99	0.92
        준하	0.82	0.84	0.97	1.00	0.85	0.71
        세형	0.98	0.63	0.99	0.85	1.00	0.98
        광희	0.98	0.47	0.92	0.71	0.98	1.00
    - 이때, 세형의 더킹에 대한 평가 점수를 예측해보고싶다면, 
        - 방법1. 세형과 가장 유사한 몇명의 점수를 이용해 예측점수로 구할 수 있음
        - 방법2. 전체를 대상으로 유사도 기반의 weighted sum 값을 예측 점수로 사용
            -> (0.98*4 + 0.63*0 + 0.99*4 + 0.85*2 + 0.98*2) / (0.98+0.63+0.99+0.85+0.98) = 2.60
    - 결과 : 세형의 더킹에 대한 평가 점수는 2.60으로 예측된다.

    [2. 아이템 기반]
    - 공조와 라라랜드의 유사도를 구하려고함 -> 이 둘을 모두 평가한 사용자는 재석,명수,세형,광희
                                          -> 공조(5, 1, 4, 4), 라라랜드(4, 1, 4, 3)
    - 유사도 : (5*4 + 1*1 + 4*4 + 4*3) / (sqrt(5*5 + 1*1 + 4*4 + 4*4) * sqrt(4*4 + 1*1 + 4*4 + 3*3) = 0.99
    - 결과 : 공조(라라랜드)를 좋아하는 사람은 라라랜드(공조)를 좋아할 확률이 높다
'''

'''
[문제점]
 - 코사인유사도는 유저마다의 개인적인 평가 성향을 반영하지 못한다 -> 피어슨 유사도
     - ex) A(5, 5, 5, 5, 5, 5), B(1, 1, 1, 1, 1, 1) : 유사도 1
 - 피어슨유사도 : 사용자의 평균 평가값ㅇ르 빼줘 문제 어느정도 해결가능
 - 적은 데이터 기반정보는 추천의 정확도를 떨어뜨릴 가능성 있음 -> 최소인원수 정하기
     - ex) 두 아이템을 모두 평가한 사람 5명 이상: 유사도 계산,
                                       5명 미만: 두 아이템에 대한 유사도 = 0
 - 보통 아이템 기반 why? 유저가 아이템을 평가하는 순간, 다른 아이템을 추천해야함
                   but, 매 평가시마다 유사도 정보를 업데이트하는 것은 현실적으로 어려움
 - 아이템 간의 관계 데이터가 발생할 확률이 높음 -> 데이터 누적될수록 추천의 정확도 높아질 것
'''

# https://movefast.tistory.com/238
# https://medium.com/sfu-cspmp/recommendation-systems-user-based-collaborative-filtering-using-n-nearest-neighbors-bf7361dc24e0
# 설명 : https://lsjsj92.tistory.com/568
# content-based filtering 설명 : https://lsjsj92.tistory.com/565

#--------------------------------------------------------------------------------------------------------------------------------------------

from math import sqrt

# [ 예시1. 피타고라스 이용 ]

'''
     가디언즈2   8월의 크리스마스   보스베이비
해도     5              4             1.5
미희    2.5             2              1
현석     ?              5              2
은비    3.5             4              5
'''

critics={
    'hhd':{'guardians of the galaxy 2':5,'christmas in august':4,'boss baby':1.5},
    'chs':{'christmas in august':5,'boss baby':2},
    'kmh':{'guardians of the galaxy 2':2.5,'christmas in august':2,'boss baby':1},
    'leb':{'guardians of the galaxy 2':3.5,'christmas in august':4,'boss baby':5}
    }

# value구하기
critics.get('hhd').get('boss baby')  # [key]: 오류발생, .get(key): None출력

# 피타고라스를 이용해 거리 계산
def sim(i, j):

    return sqrt(pow(i, 2) + pow(j, 2))

var1 =  critics['chs']['christmas in august']-critics['leb']['christmas in august']
var2 =  critics['chs']['boss baby']-critics['leb']['boss baby']
data = sim(var1,var2)

# print(data)  # 3.1622776601683795


for i in critics:
    if i!='chs': #자기자신제외
        num1 = critics.get('chs').get('christmas in august')- critics.get(i).get('christmas in august')
        num2 = critics.get('chs').get('boss baby')- critics.get(i).get('boss baby')
        # print(i," : ", 1/(1+sim(num1,num2))) #정규화
'''
정규화 전 결과: 숫자가 작아야 chs와 가까이 있는 것이다 
hhd : 1.118033988749895
kmh : 3.1622776601683795
leb : 3.1622776601683795
'''
'''
결과: hhd와 기준이 되는 chs가 가장 유사한 취향을 가짐
hhd : 0.4721359549995794
kmh : 0.2402530733520421
leb : 0.2402530733520421
'''

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

# 데이터는 무조건 가로로 옮기기
'''
userid itemid rating              Item1  Item2  Item3  Item4
 User1    A     4           User1   4             3
 User1    C     3           User2   3      3
 User2    A     3      ->   User3                        5
 User2    B     2
 User3    D     5
''' 

# 그러나 공간 낭비가 많이됨
# 사용자 기반 : 비슷한 고객들이 ~한 item을 소비했다.
    #        Item1  Item2  Item3  Item4  
    # User1
    # User2
    # User3
# 아이템 기반 : ~한 아이템을 소비한 고객들은 다음과 같은 상품도 구매했다.
    #        User1  User2  User3  User4  
    # Item1
    # Item2
    # Item3
# 보통 사용자 기반 협업 필터링보다 아이템기반 협업필터링이 더 정확도가 높음

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

# [ 예시2. collaborative_filtering -> content기반 필터링 ]

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from ast import literal_eval
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# <데이터 가지고오기>
data = pd.read_csv('../data/tmdb_5000_movies.csv')


# <전처리>
# 전처리1_사용할 데이터 추출 
data = data[['id','genres', 'vote_average', 'vote_count','popularity','title',  'keywords', 'overview']]

# 전처리2_vote_agerage변경
# why? vote수가 적은데 3개 전부 5점이라고하면 vote가 5점으로 되어있음
#      vote수가 많으면 vote_agerage가 떨어질 수밖에 없음
'''
r : 개별 영화 평점
v : 개별 영화에 평점을 투표한 횟수
m : 250위 안에 들어야 하는 최소 투표 (정하기 나름인듯. 난 500이라고 하면 500으로 해도 되고.)
c : 전체 영화에 대한 평균 평점
여기서 m은 500위로 가정하고 진행하겠습니다.
'''
# 500위 정도로 들어오게 하려면 vote_count가 상위 몇 %이어야 할까요?
# 이는 quantile을 이용해서 구할 수 있습니다.
m = data['vote_count'].quantile(0.9)  # 1838.4000000000015
data = data.loc[data['vote_count'] >= m] # 데이터갯수 529개로 거의 500개가 됨
# 상위 90%로 했을 때 481개가 들어온다

C = data['vote_average'].mean()  # vote_agerage의 평균

# vote_count에 따른 vote_agerage 가중치
def weighted_rating(x, m=m, C=C):
    v = x['vote_count']
    R = x['vote_average']
    
    return ( v / (v+m) * R ) + (m / (m + v) * C)

data['score'] = data.apply(weighted_rating, axis = 1)
#  data.head()

# list내부에 dictionary구조 (내부에 문자열로 들어가있음)
data['genres'] = data['genres'].apply(literal_eval)
data['keywords'] = data['keywords'].apply(literal_eval)

print(data)
# 우리가 알고싶은 것 : 장르가 무엇인지, 키워드가 무엇인지
data['genres'] = data['genres'].apply(lambda x : [d['name'] for d in x]).apply(lambda x : " ".join(x))
data['keywords'] = data['keywords'].apply(lambda x : [d['name'] for d in x]).apply(lambda x : " ".join(x))

# 데이터 저장
data.to_csv('./movie_data/pre_tmdb_5000_movies.csv', index = False)


# <콘텐츠 기반 필터링 추천>
data.genres.head(2)
'''
0    Action Adventure Fantasy Science Fiction
1                    Adventure Fantasy Action
Name: genres, dtype: object
'''
# 단어를 벡터화 시켜서 저장 가능
count_vector = CountVectorizer(ngram_range=(1, 3))
c_vector_genres = count_vector.fit_transform(data['genres'])
c_vector_genres.shape  # (481, 364)
# print(count_vector)
# # 코사인 유사도를 구한 벡터를 미리 저장
# # 아마 cosine유사도나 pearson중에 우리가 구현한 공식으로 하면 될듯?!
# # 영화 장르 기준 유사도
gerne_c_sim = cosine_similarity(c_vector_genres, c_vector_genres).argsort()[:, ::-1]


# 코사인 유사도를 이용해 장르가 비슷한 영화를 추천
# vote_count를 이용해서 vote_count가 높은 것을 기반으로 최종 추천
def get_recommend_movie_list(df, movie_title, top=30):
    # 특정 영화와 비슷한 영화를 추천해야 하기 때문에 '특정 영화' 정보를 뽑아낸다.
    target_movie_index = df[df['title'] == movie_title].index.values
    
    #코사인 유사도 중 비슷한 코사인 유사도를 가진 정보(영화 장르기준)를 뽑아낸다.
    sim_index = gerne_c_sim[target_movie_index, :top].reshape(-1)
    #본인을 제외
    sim_index = sim_index[sim_index != target_movie_index]

    #data frame으로 만들고 vote_count으로 정렬한 뒤 return
    result = df.iloc[sim_index].sort_values('score', ascending=False)[:10]
    return result

# The Dark Knight Rises와 비슷한 영화가 content based filtering 방법으로 추천됨
get_recommend_movie_list(data, movie_title='The Dark Knight Rises')
# The Dark Knight Rise 영화의 장르는 Action, Crime, Drama, Thriller
# -> 추천된 종류 역시 이와 같이 비슷한 장르의 특성을 보임

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

# # [ 예시3. collaborative_filtering -> item기반 필터링 ]

# # data = pd.read_csv('../data/ratings_small.csv')
# # # print(data.head())

# # # userId와 컬럼 아이디가 따로 존재했지만, 아이템기반으로 추천시스템을 만들기위해서는 
# # # user-item 테이블로 만들어야함.
# # data = data.pivot_table('rating', index = 'userId', columns = 'movieId')

# # # item별로 유사도 측정
# # movie_sim = cosine_similarity(data, data)
# # movie_sim_df = pd.DataFrame(data = movie_sim, index = data.index, columns = data.index)

# # # 특정 영화와 비교했을 때 그 영화와 유사한 영화들을 추천
# # movie_sim_df["X-Men Origins: Wolverine"].sort_values(ascending=False)[1:10]
# '''
# title
# Romeo Must Die                        0.649625
# The Wedding Planner                   0.631669
# Dogtown and Z-Boys                    0.501189
# An Unfinished Life                    0.485643
# Conquest of the Planet of the Apes    0.474626
# Reign Over Me                         0.458155
# The Terminal                          0.445337
# Young Frankenstein                    0.423840
# Whale Rider                           0.394136
# Name: X-Men Origins: Wolverine, dtype: float64
# '''


# rating_data = pd.read_csv('../data/ratings.csv')
# movie_data = pd.read_csv('../data/movies.csv')
# rating_data.dropna()  # NaN있는 행 지워줌
# # print(rating_data.head(2))

# # movieId 기준으로 합치기
# rating_data.drop('timestamp', axis = 1, inplace=True)
# user_movie_rating = pd.merge(rating_data, movie_data, on = 'movieId')
# '''
# 	userId	movieId	 rating            title	       genres
# 0	  1	      31	  2.5	  Dangerous Minds (1995)	Drama
# 1	  7	      31	  3.0	  Dangerous Minds (1995)	Drama
# '''

# movie_user_rating = pd.pivot_table(user_movie_rating, index = 'title', columns='userId')
# # user_movie_rating = user_movie_rating.pivot_table('rating', index = 'userId', columns='title')

# # print(movie_user_rating.head(2))
# # < 아이템 기반 협업필터링 > : 아이템 기반 협업 필터링은 ~ 상품을 구매한 고객들은 다음 상품도 구매했다
# # 1. NaN 값을 0으로 바꾸기
# movie_user_rating.fillna(0, inplace = True)
# print(movie_user_rating.head(2))

# # # 2. 코사인 유사도로 측정해서 확인
# # item_based_collabor = cosine_similarity(movie_user_rating)
# # item_based_collabor = pd.DataFrame(data = item_based_collabor, index = movie_user_rating.index, columns = movie_user_rating.index)

# # # 3. 특정 item에 있어 비슷한 item을 추천해주는 기능
# # def get_item_based_collabor(title):
# #     return item_based_collabor[title].sort_values(ascending=False)[:6]

# # get_item_based_collabor('Godfather, The (1972)')
# '''
# title
# Godfather, The (1972)                        1.000000
# Godfather: Part II, The (1974)               0.773685
# Goodfellas (1990)                            0.620349
# One Flew Over the Cuckoo's Nest (1975)       0.568244
# American Beauty (1999)                       0.557997
# Star Wars: Episode IV - A New Hope (1977)    0.546750
# Name: Godfather, The (1972), dtype: float64
# '''
