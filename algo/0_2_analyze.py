import itertools
from collections import Counter
from parse import load_dataframes
import pandas as pd
from datetime import datetime as dt
import shutil


def sort_stores_by_score(dataframes, n=30, min_reviews=30):
    """
    Req. 1-2-1 각 음식점의 평균 평점을 계산하여 높은 평점의 음식점 순으로 `n`개의 음식점을 정렬하여 리턴합니다
    Req. 1-2-2 리뷰 개수가 `min_reviews` 미만인 음식점은 제외합니다.
    """

    # stores 테이블의 id와 reviews테이블의 store번호가 동일하게 병합
    stores_reviews = pd.merge(
        dataframes["stores"], dataframes["reviews"], left_on="id", right_on="store"
    )
    
    # null 값을 평균값으로 채워줌
    scores_group = stores_reviews.groupby(["store", "store_name"]).mean()
    
    # 평균 평점 기준 높은 평점 음식점 순으로 정렬
    scores = scores_group.groupby(["store_name"]).mean().sort_values(by=["score"], ascending=False)
    
    # 리뷰 개수가 min_reviews 미만 음식점 제외
    # 굳이 astype(float)로 바꿀 필요가 없다 -> why? json은 int는 int대로,string은 string대로 인식하기때문
    scores = scores[scores["review_cnt"]>=30]

    # reset_index(): 인덱스 리셋 -> 새로운 단순한 정수 인덱스 세팅
    # reset_index() 작성하지 않으면 결과 보여줄 때, 인덱스가 아예 존재하지 않음
    return scores.head(n=n).reset_index()


def get_most_reviewed_stores(dataframes, n=20):
    """
    Req. 1-2-3 가장 많은 리뷰를 받은 `n`개의 음식점을 정렬하여 리턴합니다
    """
    stores_hours = pd.merge(
        dataframes["stores"], dataframes["hours"], left_on="id", right_on="store"
    )

    reviews_group = stores_hours.groupby(['store_name', 'store']).mean()

    # 리뷰 수 기준으로 정렬
    review_cnt = reviews_group.groupby(["store_name"]).mean().sort_values(by=["review_cnt"], ascending=False)

    return review_cnt.head(n=n).reset_index()


def get_most_active_users(dataframes, n=100):
    """
    Req. 1-2-4 가장 많은 리뷰를 작성한 `n`명의 유저를 정렬하여 리턴합니다.
    """
    # users와 reviews를 병합
    # 이때 users_reviews가 아닌 reviews_users로 병합하면 똑같은 리뷰가 엄청 여러개 나옴 why??????????????????    
    users_reviews = pd.merge(
        dataframes["users"], dataframes["reviews"], left_on="id", right_on="user"
    )

    users_reviews["cnt"] = 1
    # print(users_reviews.head())
    
    user_group = users_reviews.groupby('user').cnt.sum().to_frame()
    split_by_user = user_group.sort_values(by=["cnt"],ascending=False)

    return split_by_user.head(n=n).reset_index()


"""
Req 각 음식점의 평균 평점을 계산하여 높은 평점의 음식점 순으로 `n`개의 음식점을 정렬하여 리턴
    리뷰 개수가 5개 미만인 음식점은 제외하기
    리뷰갯수에 가중치 두어서 평균 평점 구하기???????????????????????? -> movie예시따라하기
       2-1. 평점 높은순으로 음식점 보여주는데 성별로 구분 V
       2-2. 평점 높은순으로 음식점 보여주는데 나이대에 따라 구분 V
       2-3. 평점 높은순으로 음식점 보여주는데 성별/나이대에 따라 구분
       2-4. 평점 높은순으로 음식점 보여주는데 지역별로 구분해서 보여주기
       2-5. 평점 높은순으로 음식점 보여주는데 음식 카테고리별로 구분해서 보여주기

Req2. 가장 많은 리뷰를 받은 `n`개의 음식점 보여주기
       3-1. 지역별로 구분해서 보여주기
       3-2. 음식 카테고리별로 구분해서 보여주기
"""


def score_by_gender(dataframes, n=60):
    '''
    Req2-1. 평점 높은순으로 음식점 보여주는데 성별로 구분(남, 여)
    '''
    users_reviews = pd.merge(
        dataframes["users"], dataframes["reviews"], left_on="id", right_on="user"
    )
    # stores는 user랑 review랑 결과 다 낸다음에 해당하는 store만 붙여야할것같다

    '''
        id_x gender born_year  id_y  store   user  score                                            content             reg_time
0  68632      남      1990     1     15  68632      5         전포 윗길에 새로 생긴! 호주에서 온 쉐프가 직접 요리하는 호주식 레스토랑!  1970-01-01 00:00:00
1  68632      남      1990   326   1216  68632      5                간단하게 먹으러 갔다가 얼큰우동에 반하고 나오는 24시 우동집!  1970-01-01 00:00:00
2  68632      남      1990  1413   8756  68632      5                     식사보다는 말그대로 피맥으로 한잔하기에 딱 좋은 피자!  1970-01-01 00:00:00
3  68632      남      1990  1528   9460  68632      5  파란 컨테이너의 외관부터 너무 이쁜 건대 커멘그래운드 2층의 루프탑카페! 분위기 좋...  2019-04-06 12:52:22
4  68632      남      1990  4681  13745  68632      5         가야공원에서 제일 맛있는 오리고기집~ 다 먹고 볶음밥 볶아 먹으면.. 크~~  2018-11-28 15:12:33

내가 필요한 것 : gender기준으로 female, male로 나누기 -> 평점 높은 순으로 음식점 보여주기
'''
# user                             |   review
# (['id_x', 'gender', 'born_year', 'id_y', 'store', 'user', 'score', 'content', 'reg_time',
# 'id', 'store_name', 'branch', 'area', 'tel', 'address', 'latitude', 'longitude', 'category', 'review_cnt'],

    # 남자 여자 구분
    male =  users_reviews[users_reviews['gender']=="남"]
    female = users_reviews[users_reviews['gender']=="여"]

    # 결측값 없고 0이 존재 -> (44785, 19) vs (44781, 19) -> 0인거 제거
    male = male[male.score != 0]
    female = female[female.score != 0]
    # 남자 집단별 평균 + 평균 평점 기준 높은 평점 음식점 순으로 정렬
    male = male.groupby('store').mean()
    male = male.sort_values(by=["score"], ascending=False)
    # 여자
    female = female.groupby('store').mean()
    female = female.sort_values(by=["score"], ascending=False)
    
    # store랑 합치기
    # 남자
    mstore = pd.merge(male, dataframes['stores'], left_on='store', right_on='id')
    mstore = mstore[mstore["review_cnt"]>=15] # 리뷰 개수가 min_reviews 미만 음식점 제외
    # 여자
    fstore = pd.merge(female, dataframes['stores'], left_on='store', right_on='id')
    fstore = fstore[fstore["review_cnt"]>=15] # 리뷰 개수가 min_reviews 미만 음식점 제외

    return mstore[['store_name', 'score']].head(n=n)


def score_by_age(dataframes, age_num, n=60):
    # 가중치 두려면 store데이터 필요
    '''
    Req2-2. 평점 높은순으로 음식점 보여주는데 나이대에 따라 구분
    '''
    users = dataframes["users"]

    # 1. 나이대 지정하기
    now = dt.now()
    this_year = now.strftime('%Y')
    this_year = int(this_year)
    users["born_year"] = users["born_year"].astype(int)
    users["age"] = this_year - users["born_year"] + 1

    bins = [0, 19, 29, 39, 49, 59, 100]
    # bins_names = ["20세미만","20대","30대","40대","50대","60세이상"]
    bins_names = [1, 2, 3, 4, 5 ,6]
    users["age_category"] = pd.cut(users["age"], bins, labels=bins_names)

    users_reviews = pd.merge(
        users, dataframes["reviews"], left_on="id", right_on="user"
    )

    # return users_reviews.head()

    # 나이대별로 구분
    people = users_reviews[users_reviews['age_category']==age_num]

    # 결측값 없고 0이 존재 -> (44785, 19) vs (44781, 19) -> 0인거 제거
    people = people[people.score != 0]
    # 집단별 평균 + 평균 평점 기준 높은 평점 음식점 순으로 정렬
    people = people.groupby('store').mean()
    # people = people.sort_values(by=["score"], ascending=False)
    
    # store랑 합치기
    pstore = pd.merge(people, dataframes['stores'], left_on='store', right_on='id')
    pstore = pstore[pstore["review_cnt"]>=5] # 리뷰 개수가 min_reviews 미만 음식점 제외  5.0 두개나옴

    # 500위 정도로 들어오게 하려면 vote_count가 상위 몇 %이어야 할까요?
    # 이는 quantile을 이용해서 구할 수 있습니다.
    m = pstore['review_cnt'].quantile(0.9)  # 1838.4000000000015
    pstore = pstore.loc[pstore['review_cnt'] >= m]

    C = pstore['score'].mean()
    
    # review_cnt 따른 score 가중치
    def weighted_rating(x, m=m, C=C):
        v = x['review_cnt']
        R = x['score']
        
        return ( v / (v+m) * R ) + (m / (m + v) * C)

    pstore['weight_score'] = pstore.apply(weighted_rating, axis = 1)
    # return pstore[['store_name', 'score']].head(n=n)
    # return pstore[['score', 'weight_score']].head()
    pstore = pstore.sort_values(by=["score"], ascending=False)
    
    return pstore[['score', 'weight_score']].head()

def score_by_area(dataframes, area_name, n=60):
    # 지역별 갯수가 200개 넘는것들이 많이 없어서 가중치 필요안할듯
    '''
    Req2-4. 평점 높은순으로 음식점 보여주는데 지역별로 구분해서 보여주기
    '''
    stores_reviews = pd.merge(
        dataframes["stores"], dataframes["reviews"], left_on="id", right_on="store"
    )
    
    # area별로 나눔
    areas = stores_reviews[stores_reviews['area']==area_name]
    
    # 결측값 없고 0이 존재 -> (44785, 19) vs (44781, 19) -> 0인거 제거
    areas = areas[areas.score != 0]
    # area별 평균 + 평균 평점 기준 높은 평점 음식점 순으로 정렬
    areas = areas.groupby('store').mean()
    areas = areas.sort_values(by=["score"], ascending=False)
    

    areas = areas[areas["review_cnt"]>=5] # 리뷰 개수가 min_reviews 미만 음식점 제외


    return areas.head(n=n)



def score_by_category(dataframes, n=10):
    '''
    Req2-5. 평점 높은순으로 음식점 보여주는데 음식 카테고리별로 구분
    '''
    ## store.csv파일로 불러와야한다,,
    stores = dataframes["stores"]

    # 모든 카테고리를 1차원 리스트에 저장합니다
    categories = stores.category.apply(lambda c: c.split("|"))
    categories = itertools.chain.from_iterable(categories)

    # 카테고리가 없는 경우 / 상위 카테고리를 추출합니다
    categories = filter(lambda c: c != "", categories)
    categories_count = Counter(list(categories))
    best_categories = categories_count.most_common(n=n)  # 가장 많은것 10개
    df = pd.DataFrame(best_categories, columns=["category", "count"]).sort_values(
        by=["count"], ascending=False
    )

    # # category별로 나눔
    # category = stores_reviews[stores_reviews['']==area_name]
    
    # # 결측값 없고 0이 존재 -> (44785, 19) vs (44781, 19) -> 0인거 제거
    # category = areas[areas.score != 0]
    # # area별 평균 + 평균 평점 기준 높은 평점 음식점 순으로 정렬
    # areas = areas.groupby('store').mean()
    # areas = areas.sort_values(by=["score"], ascending=False)
    

    # areas = areas[areas["review_cnt"]>=5] # 리뷰 개수가 min_reviews 미만 음식점 제외


    # return areas.head(n=n)


    # return df














def main():
    data = load_dataframes()
    term_w = shutil.get_terminal_size()[0] - 1
    separater = "-" * term_w

    # # 1-2-1, 1-2-2 음식점 평점 순 출력, 최소리뷰 개수 필터링
    # stores_most_scored = sort_stores_by_score(data)

    # print("[최고 평점 음식점]")
    # print(f"{separater}\n")
    # for i, store in stores_most_scored.iterrows():
    #     print(
    #         "{rank}위: {store}({score}점)".format(
    #             rank=i + 1, store=store.store_name, score=store.score
    #         )
    #     )
    # print(f"\n{separater}\n\n")


    # # 1-2-3 가장 많은 리뷰를 받은 `n`개의 음식점을 정렬
    # stores_most_review = get_most_reviewed_stores(data)

    # print("[가장 많은 리뷰를 받은 음식점]")
    # print(f"{separater}\n")
    # print(stores_most_review)


    # # 1-2-4 가장 많은 리뷰를 작성한 `n`개의 유저를 정렬
    # users_most_review = get_most_active_users(data)

    # print("[가장 많은 리뷰를 작성한 유저]")
    # print(f"{separater}\n")
    # print(users_most_review)

    # # 2-1. 평점 높은순으로 음식점 보여주기 (성별)
    # stores_most_score_by_gender = score_by_gender(data)

    # print("[평점 높은순으로 음식점 보여주는데 성별로 구분(남, 여)]")
    # print(f"{separater}\n")
    # print(stores_most_score_by_gender)

    # 2-2. 평점 높은순으로 음식점 보여주기 (나이대별로)
    stores_most_score_by_age = score_by_age(data, 3)  # 1~6중에 하나 고르기

    print("[평점 높은순으로 음식점 보여주는데 나이대에 따라 구분]")
    print(f"{separater}\n")
    print(stores_most_score_by_age)


    # 2-5. 평점 높은순으로 음식점 보여주기 (지역 카테고리별)
    # stores_most_score_by_area = score_by_area(data, '홍대')

    # print("[평점 높은순으로 음식점 보여주는데 지역별로 구분]")
    # print(f"{separater}\n")
    # print(stores_most_score_by_area)
    
    # # 2-5. 평점 높은순으로 음식점 보여주기 (음식 카테고리별)
    # stores_most_score_by_category = score_by_category(data)

    # print("[평점 높은순으로 음식점 보여주는데 음식 카테고리별로 구분]")
    # print(f"{separater}\n")
    # print(stores_most_score_by_category)


if __name__ == "__main__":
    main()

