# Example of making predictions
from math import sqrt


# 유클리드 거리 계산
def euclidean_distance(user, neighbor):
	distance = 0.0
	for i in range(len(user)-1):
		distance += (user[i] - neighbor[i])**2
	return sqrt(distance)



def get_neighbors(user, neighbor_list, k):
	distances = list()
	for neighbor in neighbor_list:
		dist = euclidean_distance(user, neighbor)
		distances.append((neighbor, dist))
	distances.sort(key=lambda tup: tup[1])  # 거리기준
	'''
	neighbors distances :  [([8, 1, 7], 1.0), ([9, 2, 9], 1.0), ([7, 2, 9], 2.23606797749979), ([2, 8, 1], 9.899494936611665), ([1, 8, 2], 10.63014581273465), ([1, 9, 1], 11.313708498984761)]
	near neighbors :  [[8, 1, 7], [9, 2, 9], [7, 2, 9]]
	predict_candidate :  [7, 9, 9]
	Predict 9.000000.
	'''
	# distances.sort()  # neighbor_list[0]이 작은 것부터
	'''
	neighbors distances :  [([1, 8, 2], 10.63014581273465), ([1, 9, 1], 11.313708498984761), ([2, 8, 1], 9.899494936611665), ([7, 2, 9], 2.23606797749979), ([8, 1, 7], 1.0), ([9, 2, 9], 1.0)]
	near neighbors :  [[1, 8, 2], [1, 9, 1], [2, 8, 1]]
	predict_candidate :  [2, 1, 1]
	Predict 1.000000.
	'''

	print('neighbors distances : ', distances)

	near_neighbors = list()
	for i in range(k):
		near_neighbors.append(distances[i][0])  # neighbors distances에서 앞에서부터 k개

	print('near neighbors : ', near_neighbors)

	return near_neighbors


def predict_classification(user, neighbor_list, k):
	neighbors = get_neighbors(user, neighbor_list, k)

	predict_candidate = [row[-1] for row in neighbors]
	print('predict_candidate : ', predict_candidate)
	prediction = max(set(predict_candidate), key=predict_candidate.count)
	return prediction

# Test distance function




k = 3
user = [9, 1, 0]
neighbor_list = [
	[2,8,1],
	[7,2,9],
	[8,1,7],
	[1,9,1],
	[9,2,9],
	[1,8,2]]

prediction = predict_classification(user, neighbor_list, k)

print('Predict %f.' % (prediction))
'''
neighbors distances :  [([8, 1, 7], 1.0), ([9, 2, 9], 1.0), ([7, 2, 9], 2.23606797749979), ([2, 8, 1], 9.899494936611665), ([1, 8, 2], 10.63014581273465), ([1, 9, 1], 11.313708498984761)]
near neighbors :  [[8, 1, 7], [9, 2, 9], [7, 2, 9]]
predict_candidate :  [7, 9, 9]
Predict 9.000000.
'''

