# @Time    : 28/7/20 11:43
# @Author  :  KarKin
# @FileName: worker.py

import pickle
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


class LinearModel(object):

    def __init__(self, dataset, path = None):
        
        self.model_path = path
        
        if not path:
            self.model = LinearRegression()
            self.dataset = dataset
        else:
            with open(path, 'rb') as f:
                self.model = pickle.load(f)    

    def train(self):

        if self.model_path:
            return 

        x = self.dataset.data
        y = self.dataset.target
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=5)
        self.model.fit(x_train, y_train)

        with open('./algo/linear_regression.pkl', 'wb') as f:
            pickle.dump(self.model, f)




model = LinearModel(datasets.load_boston())
model.train()

