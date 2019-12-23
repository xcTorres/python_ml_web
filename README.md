# Machine Learning Python Web Service 

python_web is a sample python web service for machine learning, the sample model in this repo is linear regression. Because [flask](https://www.palletsprojects.com/p/flask/) its own WSGI server is very simple and can not be used in production environment, So people often use gunicorn or other WSGI server to manage the flask web application.  
[Gunicorn](https://gunicorn.org/) has a master worker, which can manage all of other slave workers. Every slave workers handle one flask application. In case master worker crash, we can utilize [supervisor](https://github.com/Supervisor/supervisor) to monitor all of gunicorn workers, and it will restart when workers die.  

what I have done in optimisation in this multi process mode are as follows.  

---   

1. if we wanna load a machine learning model, we cannot load it in flask web application. Otherwise it will consume the memory of worker numbers multiply per model memory. The alternative plan is that we can load the model in gunicorn.conf file, which will be loaded only once in master worker and  the model can be passed to any of slave workers by pre_request hook function.  

2. we know that logging is very important for tracking the issues and bugs. But for python built-in TimedRotatingFileHandler, it cannot run normally in multi-processing mode. So SafeRotatingFileHandler is born, it is in algo.util directory, just add a multi processing lock, in case the new comming info is put into the old log file.

## Build 

```shell script

    docker build -t python_web -f Dockerfile . 

    docker run -it --rm \
                    -p  8020:8020 \
                    -e WORKERS=2 \
                    python_web

```

## Test
```shell script
    curl http://127.0.0.1:8020/pricing?CRIM=2.8&ZN=10.211&INDUS=18.237
```
