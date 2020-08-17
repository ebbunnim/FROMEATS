'''
[코사인 유사도]
1. 의미
   -1: 백터의 방향이 서로 완전히 반대
    0: 독립
    1:완전히 같은방향
2. 사용
 - 사용자1과 사용자2 간의 유사도, 상품i와 상품j의 유사도
   -> 두 사용자가 모두 평가한 상품의 평점을 사용해 계산
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import wikipediaapi   # pip install wikipedia-api
# 문서 전처리용 sklearn
from sklearn.feature_extraction.text import CountVectorizer  # pip install scikit-learn

# [ 기본 코사인 유사도 ]
X = np.array([[6.6, 6.2, 1],
              [9.7, 9.9, 2],
              [8.0, 8.3, 2],
              [6.3, 5.4, 1],
              [1.3, 2.7, 0],
              [2.3, 3.1, 0],
              [6.6, 6.0, 1],
              [6.5, 6.4, 1],
              [6.3, 5.8, 1],
              [9.5, 9.9, 2],
              [8.9, 8.9, 2],
              [8.7, 9.5, 2],
              [2.5, 3.8, 0],
              [2.0, 3.1, 0],
              [1.3, 1.3, 0]])

df = pd.DataFrame(X, columns=['weight', 'length', 'label'])
ax = df[df['label'] == 0].plot.scatter(x='weight', y='length', c='blue', label='young')
ax = df[df['label'] == 1].plot.scatter(x='weight', y='length', c='orange', label='mid', ax=ax)
ax = df[df['label'] == 2].plot.scatter(x='weight', y='length', c='red', label='adult', ax=ax)
# plt.show()

df2 = pd.DataFrame([df.iloc[0], df.iloc[1], df.iloc[4]], columns=['weight', 'length', 'label'])
df3 = pd.DataFrame([df.iloc[14]], columns=['weight', 'length', 'label'])

ax = df2[df2['label'] == 0].plot.scatter(x='weight', y='length', c='blue', label='young')
ax = df2[df2['label'] == 1].plot.scatter(x='weight', y='length', c='orange', label='mid', ax=ax)
ax = df2[df2['label'] == 2].plot.scatter(x='weight', y='length', c='red', label='adult', ax=ax)
ax = df3.plot.scatter(x='weight', y='length', c='gray', label='?', ax=ax)
# plt.show()

def euclidean_distance(x, y):   
    return np.sqrt(np.sum((x - y) ** 2))

x0 = X[0][:-1]
x1 = X[1][:-1]
x4 = X[4][:-1]
x14 = X[14][:-1]
print(" x0:", x0, "\n x1:", x1, "\n x4:", x4, "\nx14:", x14)

print(" x14 and x0:", euclidean_distance(x14, x0), "\n",
      "x14 and x1:", euclidean_distance(x14, x1), "\n",
      "x14 and x4:", euclidean_distance(x14, x4))

def cosine_similarity(x, y):
    # x * y / sqrt(x * x) * sqrt(y * y)
    return np.dot(x, y) / (np.sqrt(np.dot(x, x)) * np.sqrt(np.dot(y, y)))

print(" x14 and x0:", cosine_similarity(x14, x0), "\n",
      "x14 and x1:", cosine_similarity(x14, x1), "\n",
      "x14 and x4:", cosine_similarity(x14, x4))

'''
[when 코사인 유사도 사용?]
 - 벡터의 크기가 중요하지 않을 때 거리측정
 - 단어의 포함 여부로 문서의 유사 여부를 판단한다고 할때 ‘science’라는 단어가 2번 보다 1번 문서에 더 많이 포함되어 있다면
   1번 문서가 과학 문서라고 추측할 수 있을 것이다. 그러나, 만약 1번 문서가 2번 문서 보다 훨씬 더 길다면 공정하지 않은 비교가 된다.
   이때 코사인 유사도는 이 문제를 바로 잡아줄 수 있다.
'''

# [ 위키피디아 실제 예제 ]
wiki = wikipediaapi.Wikipedia('en')

q1 = wiki.page('Machine Learning')
q2 = wiki.page('Artifical Intelligence')
q3 = wiki.page('Soccer')
q4 = wiki.page('Tennis')

q1.text[:100]
q1.text.split()[:10]

# 각각의 본문 -> 문서의 길이 모두 다름!
# print("ML \t", len(q1.text.split()), "\n"
#       "AI \t", len(q2.text.split()), "\n"
#       "soccer \t", len(q3.text.split()), "\n"
#       "tennis \t", len(q4.text.split()))

# k-hot vector로 인코딩
cv = CountVectorizer()  # 문서 집합에서 단어 토큰을 생성하고 각 단어의 수를 세어 BOW 인코딩한 벡터 생성
# 전체 단어수 만큼의 배열 -> 각각의 값은 해당 단어의 출현 빈도를 나타냄
X = np.array(cv.fit_transform([q1.text, q2.text, q3.text, q4.text]).todense())
xx1 = X[0].shape  # (5857,)
xx2 = X[0][:20]  # [0 0 0 0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]

# 문서들간의 유사도를 유클리드 거리로 나타내기
print("ML - AI \t", euclidean_distance(X[0], X[1]), "\n"
      "ML - soccer \t", euclidean_distance(X[0], X[2]), "\n"
      "ML - tennis \t", euclidean_distance(X[0], X[3]))

'''
결과해석 : ML문서는 축구와 갖아 가깝고 AI랑 가장 멀다
            -> 이는 문서의 길이가 다르기 때문 
ML - AI          818.8815543166179
ML - soccer      457.3270164772687
ML - tennis      796.3755395540474
'''

# 문서들간의 유사도를 코사인 유사도로 비교하기
print("ML - AI \t", cosine_similarity(X[0], X[1]), "\n"
      "ML - soccer \t", cosine_similarity(X[0], X[2]), "\n"
      "ML - tennis \t", cosine_similarity(X[0], X[3]))
'''    
결과해석 : 유클리드 거리와는 정반대의 결과
ML - AI          0.8954582208238121
ML - soccer      0.8012467981878524
ML - tennis      0.8126178227188197
'''

# 문서의 길이를 정규화한 후, 유클리드 거리로 비교
def l2_normalize(v):
    norm = np.sqrt(np.sum(np.square(v)))
    return v / norm

print("ML - AI \t", 1 - euclidean_distance(l2_normalize(X[0]), l2_normalize(X[1])), "\n"
      "ML - soccer \t", 1 - euclidean_distance(l2_normalize(X[0]), l2_normalize(X[2])), "\n"
      "ML - tennis \t", 1 - euclidean_distance(l2_normalize(X[0]), l2_normalize(X[3])))
'''
결과 : 코사인 유사도와 값은 다르지만 패턴은 일치
ML - AI 	       0.5283996828641448 
ML - soccer 	 0.3426261066509869 
ML - tennis 	 0.3574544240773757
'''


# [ 트위터 분류 ]
ml_tweet = "New research release: overcoming many of Reinforcement Learning's limitations with Evolution Strategies."
x = np.array(cv.transform([ml_tweet]).todense())[0]

# 오픈 ai의 트윗 - 유클리드
print("tweet - ML \t", euclidean_distance(x, X[0]), "\n"
      "tweet - AI \t", euclidean_distance(x, X[1]), "\n"
      "tweet - soccer \t", euclidean_distance(x, X[2]), "\n"
      "tweet - tennis \t", euclidean_distance(x, X[3]))
'''
결과: 축구가 ai보다 가깝다고 나옴 -> 잘못됨
tweet - ML       581.5530930190296
tweet - AI       1297.6135788438714
tweet - soccer   762.4421289514372
tweet - tennis   1193.2971130443582
'''

# 코사인 유사도
print("tweet - ML \t", cosine_similarity(x, X[0]), "\n"
      "tweet - AI \t", cosine_similarity(x, X[1]), "\n"
      "tweet - soccer \t", cosine_similarity(x, X[2]), "\n"
      "tweet - tennis \t", cosine_similarity(x, X[3]))
'''
결과 : ai, ml이 축구보다 더 높은 값을 나타냄
tweet - ML       0.2470841802882599
tweet - AI       0.19267637521513586
tweet - soccer   0.1181486847316886
tweet - tennis   0.11312292263257678
'''


# 정규화해 유클리드 거리로 비교
print("tweet - ML \t", 1 - euclidean_distance(l2_normalize(x), l2_normalize(X[0])), "\n"
      "tweet - AI \t", 1 - euclidean_distance(l2_normalize(x), l2_normalize(X[1])), "\n"
      "tweet - soccer \t", 1 - euclidean_distance(l2_normalize(x), l2_normalize(X[2])), "\n"
      "tweet - tennis \t", 1 - euclidean_distance(l2_normalize(x), l2_normalize(X[3])))
'''
결과 : ai가 축구보다 더 높은 값을 나타냄
tweet - ML       -0.22712331875141234
tweet - AI       -0.2706877073339964
tweet - soccer   -0.32804466436058655
tweet - tennis   -0.33182361997932985
'''
