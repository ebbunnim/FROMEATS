'''
우리가 가지고 있는 데이터 -> store, menu, hour, review, user
1. 유저에게 음식점 추천 가능 / 카테고리 추천 가능?
     store.name
user review.score

2. 위치기반 음식점 추천 -> 상위10개 + 분류단위10개
     store.name
위치 review.score

3. 하나의 가게를 눌렀을 때, 이와 유사한 가게 보여주기
 - 기준 : 카테고리 -> 평점 -> 위치 
'''

from parse import load_dataframes
import pandas as pd
import numpy as np
import shutil
import math
import matplotlib.pyplot as plt
import seaborn as sns
from ast import literal_eval
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = load_dataframes()
term_w = shutil.get_terminal_size()[0] - 1
separater = "-" * term_w

# 코사인 유사도
def cosine_similarity_func(x, y):
    # x * y / sqrt(x * x) * sqrt(y * y)
    return np.dot(x, y) / (np.sqrt(np.dot(x, x)) * np.sqrt(np.dot(y, y)))

# 피어슨 유사도
def sim_pearson(data, name1, name2):
    avg_name1 = 0
    avg_name2 = 0
    count = 0
    for movies in data[name1]:
        if movies in data[name2]: #같은 영화를 봤다면
            avg_name1 = data[name1][movies]
            avg_name2 = data[name2][movies]
            count += 1
    
    avg_name1 = avg_name1 / count
    avg_name2 = avg_name2 / count
    
    sum_name1 = 0
    sum_name2 = 0
    sum_name1_name2 = 0
    count = 0
    for movies in data[name1]:
        if movies in data[name2]: #같은 영화를 봤다면
            sum_name1 += pow(data[name1][movies] - avg_name1, 2)
            sum_name2 += pow(data[name2][movies] - avg_name2, 2)
            sum_name1_name2 += (data[name1][movies] - avg_name1) * (data[name2][movies] - avg_name2)
    
    return sum_name1_name2 / (math.sqrt(sum_name1)*math.sqrt(sum_name2))


################### 유저에게 음식점 추천 ########################################################################################################
'''
store  1  2  3  4 
user1  5  4  ?  2 
user2  3  4  5  3   -> 이때 ?는?
user3  4  3  4 
'''

reviews = data["reviews"]
'''
   id    store     user    score                                            content                                               reg_time
0   1     15      68632      5         전포 윗길에 새로 생긴! 호주에서 온 쉐프가 직접 요리어요 가성비 추천하는 호주식 레스토랑!  1970-01-01 00:00:00
1   2     18     389728      5                    샌드위치 내용물도 알차게 들어있고 맛있었어요 가성비 추천                      1970-01-01 00:00:00
2   3     19      68716      4  홈플러스 1층 매장 푸드코트 내 있는 매장인데 계란찜정식은 처음보고 시켜봣는데 사진...             1970-01-01 00:00:00
3   4     37     774353      2  전 여기 5년전에 가봤었는데 그때 기억은 별로였어요\n단체손님이 많았고, 차려지는건...              1970-01-01 00:00:00
4   5     38     115682      3  친구들끼리 술 간단하게마시러 감. 스끼다시 괜찮지만 회 양이 조금 부족한 느낌. 맛...               2019-03-15 22:16:47
'''

# 위의 표처럼 만들기
reviews['store'] = reviews['store'].astype(str)
reviews['user'] = reviews['user'].astype(str)
# reviews['score'] = reviews['score'].astype(str)
df = pd.pivot_table(reviews, values='score', index='user', columns='store')

# NaN인 곳은 0.0으로 처리
df.fillna(0, inplace = True)
# print(df.head(2))
'''
store  100002  100014  100030  100040  100055  ...  99956  99957  99971  99975  99981
user                                           ...
10008     0.0     0.0     0.0     0.0     0.0  ...    0.0    0.0    0.0    0.0    0.0
1001      0.0     0.0     0.0     0.0     0.0  ...    0.0    0.0    0.0    0.0    0.0
'''

# 유사도 측정
user_similarity = cosine_similarity(df, df)
print(user_similarity.head(2))
# user_sim_df = pd.DataFrame(data=user_similarity, index=data.user, columns=data.store)
# user_sim_df.head(3)

