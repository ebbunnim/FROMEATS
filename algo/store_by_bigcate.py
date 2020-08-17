import itertools
from collections import Counter
# from category import load_dataframes
import pandas as pd
from datetime import datetime as dt
from parse import load_dataframes
import shutil

def score_by_category(dataframes, n=10):
    '''
    Req2-5. 평점 높은순으로 음식점 보여주는데 음식 카테고리별로 구분
    '''
    # store.csv파일로 불러와야한다,,
    stores = dataframes["stores"]

    

    # # category별로 나눔
    # category = stores_reviews[stores_reviews['']==area_name]
    
    # # 결측값 없고 0이 존재 -> (44785, 19) vs (44781, 19) -> 0인거 제거
    # category = areas[areas.score != 0]
    # # area별 평균 + 평균 평점 기준 높은 평점 음식점 순으로 정렬
    # areas = areas.groupby('store').mean()
    # areas = areas.sort_values(by=["score"], ascending=False)
    

    # areas = areas[areas["review_cnt"]>=5] # 리뷰 개수가 min_reviews 미만 음식점 제외


    return stores.head(n=n)



def main():
    data = load_dataframes()
    term_w = shutil.get_terminal_size()[0] - 1
    separater = "-" * term_w

    print("[평점 높은순으로 음식점 보여주는데 음식 카테고리별로 구분]")
    print(f"{separater}\n")
    print(score_by_category)

if __name__ == "__main__":
    main()
