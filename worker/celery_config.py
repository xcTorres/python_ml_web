# @Time    : 22/7/20 17:35
# @Author  :  xcTorres
# @FileName: celery_config.py


broker_url = 'pyamqp://guest:guest@{}:{}//' \
    .format(
        'rabbitmq',
        5672
        )

broker_heartbeat = 0
broker_pool_limit = 100
result_backend = 'redis://redis:6379'
result_compression = 'gzip'
result_expires = 60
redis_max_connections = 1000
redis_socket_connect_timeout = 300
redis_socket_timeout = 120

task_serializer = 'json'
task_acks_late = True
task_compression = 'gzip'
task_default_delivery_mode = 1

accept_content = ['json']

# only give 1 task per worker so the task will be evenly distributed
worker_prefetch_multiplier = 5
timezone = 'Asia/Singapore'
enable_utc = True

