# use knn

from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from parse import load_dataframes
import numpy as np
import shutil
import os

data = load_dataframes()
term_w = shutil.get_terminal_size()[0] - 1
separater = "-" * term_w

menu = data["menus"]
# print(menu.head())
menu.to_excel("../Data/menu.xlsx", sheet_name="Sheet1", index=True)


# x_train, x_test, y_train, y_test = \
# train_test_split(iris.data, iris.target, test_size=0.3, random_state=0)

# knn = KNeighborsClassifier(n_neighbors=1, n_jobs=-1)
# knn.fit(x_train, y_train)

# x_sample = np.array([[5, 2.9, 1, 0.2]])
# prediction = knn.predict(x_sample)
# results = {p:n for p, n in zip(prediction, iris.target_names[prediction])}
# print('sample test ==> {}'.format(results))


