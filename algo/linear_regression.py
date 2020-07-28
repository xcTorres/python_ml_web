# @Time    : 21/12/19 13:02
# @Author  :  xcTorres
# @FileName: linear_regression.py

import numpy as np
import pickle
from algo import logger
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

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

        with open('algo/linear_regression.pkl', 'wb') as f:
            pickle.dump(self.model, f)    

        # model evaluation for training set
        y_train_predict = self.model.predict(x_train)
        rmse = (np.sqrt(mean_squared_error(y_train, y_train_predict)))
        r2 = r2_score(y_train, y_train_predict)

        logger.info("The model performance for training set")
        logger.info('RMSE is {}'.format(rmse))
        logger.info('R2 score is {}'.format(r2))

        # model evaluation for testing set
        y_test_predict = self.model.predict(x_test)
        rmse = (np.sqrt(mean_squared_error(y_test, y_test_predict)))
        r2 = r2_score(y_test, y_test_predict)

        logger.info("The model performance for testing set")
        logger.info('RMSE is {}'.format(rmse))
        logger.info('R2 score is {}'.format(r2))

    def predict(self, x):
        y_predict = self.model.predict(x)
        return y_predict



