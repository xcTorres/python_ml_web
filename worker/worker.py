# @Time    : 22/7/20 17:43
# @Author  :  xcTorres
# @FileName: worker.py

from celery import Celery
from worker import celery_config
from algo.linear_regression import LinearModel
from sklearn import datasets

celery = Celery(broker=celery_config.broker_url)
celery.config_from_object(celery_config)

model = None


@celery.task(hard_time_limit=2)
def process(data):
    global model
    if not model:
        model = LinearModel(datasets.load_boston())
        model.train()
    res = model.predict(data['x'])
    return res.tolist()
