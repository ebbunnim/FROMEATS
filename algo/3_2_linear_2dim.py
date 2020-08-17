'''
y = W * x + b (x: 몸무게, 나이 / y: 키)
몸무게 나이 키
 5.0   50  13.0
 6.0   20  15.5
10.0   30  22.5
 7.0   40  17.0
 8.0   20  20.0
12.0   60  26.5
 9.0   40   ?

?를 식에따라서 구함 
'''
import numpy as np

def LinearRegression(X, Y, iteration):

    # X.T -> X의 전치행렬
    weight = np.zeros((1, len(X.T)))  # zeros는 0으로 넣는다
    bias = np.zeros((1, 1))  #[0]
    Y = Y.reshape(-1,1)
      # reshape(a, b) = a * b로 행렬 정렬
      # 원래 행렬=1*12 -> reshape(-1, 1) = shape(12,1)

    learning_rate = 1e-4

    for i in range(iteration):
        # error = Y값 - 우리가 추정한 직선에서의 값    
        error = Y - prediction(weight, bias, X)

        weight_delta, bias_delta = gradient(X, error, learning_rate)
        weight -= weight_delta
        bias -= bias_delta

    return weight, bias

# prediction:
def prediction(weight, bias, X):

    return np.dot(X, weight.T) + bias  # X * weight의 전치행렬 + bias


# gradient : x 방향으로의 편미분 값과 y 방향으로의 편미분 값을 원소로 하는 벡터를 출력
def gradient(X, error, learning_rate):

    weight_delta = -(learning_rate * (1 / len(error)) * (np.dot(X.T, error)))
    bias_delta = -(learning_rate * 100 * len(error) * np.sum(error))

    return weight_delta.T, bias_delta


X = np.array([[5.0, 50], [6.0, 20], [10.0, 30], [7.0, 40], [8.0, 20], [12.0, 60]])
Y = np.array([13.0, 15.5, 22.5, 17.0, 20.0, 26.5])
iteration = 100000  # 몇번 반복해서 W를 찾을 것인지!!

weight, bias  = LinearRegression(X, Y, iteration)

print('weight  : ', weight)
print('bias  : ', bias)

X_test = np.array([[9.0, 40]])  # x값이 주어졌으니까 ?를 구해라!!

predicted_Y = prediction(weight, bias, X_test)

print('X : ', X_test, ', predicted Y : ', predicted_Y)

'''
weight  :  [[ 1.92580379 -0.0211047 ]]
bias  :  [[4.45074196]]
X :  [[ 9. 40.]] , predicted Y :  [[20.93878813]]
'''