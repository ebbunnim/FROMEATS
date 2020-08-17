import os
import pandas as pd
from surprise import SVD
from surprise import Dataset
from surprise import dump


data = Dataset.load_builtin('ml-100k')
print(data)
# df = pd.DataFrame(data.raw_ratings, columns=["user", "item", "rate", "id"])