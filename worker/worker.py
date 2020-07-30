# @Time    : 22/7/20 17:43
# @Author  :  xcTorres
# @FileName: worker.py
import time

from celery import Celery
from algo.train_model import model
from worker import celery_config


celery = Celery(broker=celery_config.broker_url)
celery.config_from_object(celery_config)


@celery.task(hard_time_limit=2)
def process(data):
    res = model.model.predict(data['x'])
    time.sleep(0.02)
    return res.tolist()
