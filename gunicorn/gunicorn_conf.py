import os

LOCAL_HOST = "0.0.0.0"

workers = os.environ.get("WORKERS", 1)
worker_class = os.environ.get("WORKER_CLASS", "gevent")
worker_connections = os.environ.get("WORKER_CONNECTIONS", 1000)
port = os.environ.get("PORT", 8020)
bind = ':'.join([LOCAL_HOST, str(port)])
timeout = os.environ.get("TIME_OUT", 120)

# pidfile = '/var/run/gunicorn.pid'
# accesslog = '/var/log/gunicorn_acess.log'
# errorlog = '/var/log/gunicorn_error.log'
loglevel = 'info'


print("Workers Num: {}".format(workers))
print("Workers Class: {}".format(worker_class))
print("Bind: {}".format(bind))
print("Timeout: {}".format(timeout))


