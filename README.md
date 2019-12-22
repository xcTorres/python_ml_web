# Machine Learning Python Web Service 

python_web is a sample python web service for machine learning, the sample model that I choose is linear regression. Because flask its own WSGI server is very simple and can not be used in production environment, So people often use gunicorn or other WSGI server to manage the flask web application, which is a multi process pre-fork tool.   
Gunicorn has a master worker, which can manages all of other slave workers. And every slave workers handle one flask application. what I have done in optimisation in multi process mode are as follows.  
1. if we wanna load a machine learning model, we cannot load it in flask web application. Otherwise, it will consume the memory of worker numbers multiply per model memory. But  we can load the model in gunicorn.conf file, which will be loaded only once in master worker, the model can be passed by pre_request hook function.  
2. we know that logging is very important for tracking the issues and bugs. But for python built-in TimedRotatingFileHandler, it cannot run normally in multi-processing mode. So SafeRotatingFileHandler is born, it is very simple, just add a multi processing lock, in case the new comming info is put into the log file that just is rolled over.

## Build 

```shell script

    docker build -t python_web -f Dockerfile . 

    docker run -it --rm \
                    -p  8020:8020 \
                    -e WORKERS=2 \
                    python_web

```