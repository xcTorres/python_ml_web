import os
import multiprocessing

LOCAL_HOST = '127.0.0.1'

workers = os.environ.get("WORKERS", multiprocessing.cpu_count() * 2 + 1)
worker_class = os.environ.get("WORKER_CLASS", "sync")

port = os.environ.get("PORT", 5000)
bind = LOCAL_HOST.join('.').join(str(port))
time_out = os.environ.get("TIME_OUT", 120)

pidfile = '/var/run/gunicorn.pid'
accesslog = '/var/log/gunicorn_acess.log'
errorlog = '/var/log/gunicorn_error.log'
loglevel = 'info'