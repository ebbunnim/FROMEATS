import itertools
from parse import load_dataframes
from collections import Counter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from ast import literal_eval
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import NearestNeighbors
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, cross_val_score
# import mglearn
from sklearn.metrics.pairwise import cosine_similarity
from datetime import datetime as dt
import shutil
import os

data = load_dataframes()
term_w = shutil.get_terminal_size()[0] - 1
separater = "-" * term_w

# 데이터 필요한것만
users = data["users"]

stores = data["stores"]
print(stores.shape)
# for col in stores.columns:
#     if col == "branch" or col == "area" or col == "tel" or col == "address" or col == "latitude" or col == "longitude" or col == "review_cnt":
#         del stores[col]

# reviews = data["reviews"]
# for col in reviews.columns:
#     if col == "score" or col == "content" or col == "reg_time":
#         del reviews[col]

# menus = data["menus"]

# # 1. 나이대 지정하기
# now = dt.now()
# this_year = now.strftime('%Y')
# this_year = int(this_year)
# users["born_year"] = users["born_year"].astype(int)
# users["age"] = this_year - users["born_year"] + 1

# bins = [0, 19, 29, 39, 49, 59, 100]
# # bins_names = ["20세미만","20대","30대","40대","50대","60세이상"]
# bins_names = [1, 2, 3, 4, 5 ,6]
# users["age_category"] = pd.cut(users["age"], bins, labels=bins_names)

# stores_reviews = pd.merge(
#         data["stores"], data["reviews"], left_on="id", right_on="store"
# )

# stores_reviews_users = pd.merge(
#         stores_reviews, data["users"], left_on="user", right_on="id"
# )

# stores_reviews_users_menus = pd.merge(
#         stores_reviews_users, data["menus"], left_on="store", right_on="store"
# )
# # print(stores_reviews_users_menus.head())
# # print(menus.head())


# # 카테고리랑 연령, 메뉴가격으로 카테고리 나눈다...
# use_data = stores_reviews_users_menus[["store_name", "category", "store", "gender", "age_category", "price"]]
# print(use_data.shape)
# X = use_data["category"].to_numeric()
# use_data["category"]
# print(use_data.head())
'''
     store_name   category   store   gender     age_category    price
0    24시 우동집              1216      남            3         3000.0
1     hTTp피맥    피자|맥주   8756      남            3         18000.0
2     hTTp피맥    피자|맥주   8756      남            3         15000.0
3     hTTp피맥    피자|맥주   8756      남            3         13000.0
4     hTTp피맥    피자|맥주   8756      남            3         16000.0
'''
# y = use_data["age_category"]
# x_train, x_test, y_train, y_test = train_test_split(X, y, random_state=30)
# clf = KNeighborsClassifier()
# clf.fit(x_train, y_train)
# prediction = clf.predict(x_test)
# print("clf.score             : {0:.3f}".format(clf.score(x_train, y_train)))
# print("(pred == y_test) score: {0:.3f}".format((prediction==y_test).mean()))
# print("cross_val_score       : {0:.3f}".format(cross_val_score(clf, x_train, y_train, cv=10).mean()))

# mglearn.plots.plot_knn_classification(n_neighbors=1)

# 모든 카테고리를 1차원 리스트에 저장합니다
# categories = stores.category.apply(lambda c: c.split("|"))
# categories = itertools.chain.from_iterable(categories)
# print(categories)
# # 카테고리가 없는 경우 / 상위 카테고리를 추출합니다
# categories = filter(lambda c: c != "", categories)
# categories_count = Counter(list(categories))

# use_data["cate"] = categories_count
# print(use_data.head())
# # best_categories = categories_count.most_common(n=n)  # 가장 많은것 10개
# # df = pd.DataFrame(best_categories, columns=["category", "count"]).sort_values(
# #     by=["count"], ascending=False
# # )

# # print(categories_count)
# # 내가원하던 카테고리 전체
# category = pd.DataFrame.from_dict(categories_count, orient='index').reset_index()

# category_name = category['index'].tolist()

# count_category = CountVectorizer(ngram_range=(1, 3))
# c_vector_category = count_category.fit_transform(category['index'])

# category_c_sim = cosine_similarity(c_vector_category, c_vector_category).argsort()[:, ::-1]
