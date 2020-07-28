# @Time    : 28/7/20 11:43
# @Author  :  KarKin
# @FileName: worker.py

from sklearn import datasets
from linear_regression import LinearModel

model = LinearModel(datasets.load_boston())
model.train()