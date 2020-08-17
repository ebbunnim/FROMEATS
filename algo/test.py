from parse import load_dataframes
import pandas as pd
import numpy as np
import shutil

data = load_dataframes()
term_w = shutil.get_terminal_size()[0] - 1
separater = "-" * term_w

stores_reviews = pd.merge(
        data["stores"], data["reviews"], left_on="id", right_on="store"
    )

areas = stores_reviews[stores_reviews.score != 0]
areas = areas[areas['area']=='연남동']

# 500위 정도로 들어오게 하려면 vote_count가 상위 몇 %이어야 할까요?
# 이는 quantile을 이용해서 구할 수 있습니다.
m = areas['review_cnt'].quantile(0.9)  # 1838.4000000000015
areas = areas.loc[areas['review_cnt'] >= m] # 데이터갯수 529개로 거의 500개가 됨
# 상위 90%로 했을 때 481개가 들어온다

print(areas.shape)



def score_by_area(dataframes, area_name, n=60):
    '''
    Req2-4. 평점 높은순으로 음식점 보여주는데 지역별로 구분해서 보여주기
    '''
    stores_reviews = pd.merge(
        dataframes["stores"], dataframes["reviews"], left_on="id", right_on="store"
    )

     # 결측값 없고 0이 존재(미실시) -> 0인거 제거
    areas = stores_reviews[stores_reviews.score != 0]
    areas = areas[areas['area']==area_name]

    # 500위 정도로 들어오게 하려면 vote_count가 상위 몇 %이어야 할까요?
    # 이는 quantile을 이용해서 구할 수 있습니다.
    m = areas['review_cnt'].quantile(0.9)  # 1838.4000000000015
    areas = areas.loc[areas['review_cnt'] >= m] # 데이터갯수 529개로 거의 500개가 됨
    # 상위 90%로 했을 때 481개가 들어온다

    C = areas['score'].mean()  # vote_agerage의 평균

    # review_cnt 따른 score 가중치
    def weighted_rating(x, m=m, C=C):
        v = x['review_cnt']
        R = x['score']
        
        return ( v / (v+m) * R ) + (m / (m + v) * C)

    areas['weight_score'] = areas.apply(weighted_rating, axis = 1)
    