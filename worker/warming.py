# @Time    : 24/7/20 14:18
# @Author  :  xcTorres
# @FileName: warming.py


"""The purpose of this python script is to do container-wise warm-up check
before starting gunicorn, specifically we check the readiness of jvm and redis container.
"""
import time
from algo import logger
from kombu.connection import Connection
from worker.celery_config import broker_url, result_backend

TRY_CONNECT_INTERVAL = 1

# check rabbitmq server
is_connected = False
trial_num = 1
while not is_connected:
    try:
        conn = Connection(broker_url,
                          transport_options={
                              'max_retries': 1
                          })
        if conn.connect():
            is_connected = True
            conn.release()
        print(time.strftime('%c', time.localtime()))
    except Exception as e:
        if (trial_num % 5) == 0:
            logger.warning('rabbitmq connection failed at trial {}'.format(trial_num))
    finally:
        time.sleep(TRY_CONNECT_INTERVAL)
        trial_num += 1
logger.info("rabbitmq connected successfully")


# check redis server
is_connected = False
redis_trial = 1
while not is_connected:
    try:
        conn = Connection(result_backend,
                          transport_options={
                              'max_retries': 1
                          })
        if conn.connect():
            is_connected = True
            conn.release()
        print(time.strftime('%c', time.localtime()))
    except Exception as e:
        if (redis_trial % 5) == 0:
            logger.warning('redis connection failed at trial {}'.format(redis_trial))
    finally:
        time.sleep(TRY_CONNECT_INTERVAL)
        redis_trial += 1

logger.info("redis connected successfully")

