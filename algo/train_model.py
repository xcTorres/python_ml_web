# @Time    : 28/7/20 11:43
# @Author  :  KarKin
# @FileName: worker.py

import os

print(os.getcwd())
print(os.listdir())

from sklearn import datasets
from algo.linear_regression import LinearModel

model = LinearModel(datasets.load_boston())
model.train()