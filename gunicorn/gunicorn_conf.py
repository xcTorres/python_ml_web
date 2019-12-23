import os
import multiprocessing
from algo.linear_regression import LinearModel
from sklearn import datasets

LOCAL_HOST = "0.0.0.0"

workers = os.environ.get("WORKERS", 5)
worker_class = os.environ.get("WORKER_CLASS", "sync")
port = os.environ.get("PORT", 8020)
bind = ':'.join([LOCAL_HOST, str(port)])
time_out = os.environ.get("TIME_OUT", 120)

pidfile = '/var/run/gunicorn.pid'
accesslog = '/var/log/gunicorn_acess.log'
errorlog = '/var/log/gunicorn_error.log'
loglevel = 'info'


model = LinearModel(datasets.load_boston())
model.train()

print("Workers Num: {}".format(workers))
print("Workers Class: {}".format(worker_class))
print("Bind: {}".format(bind))
print("Timeout: {}".format(time_out))

def pre_request(worker, req):
    req.headers.append(('MODEL', model))  # transfer the model to flask workers.

pre_request = pre_request


