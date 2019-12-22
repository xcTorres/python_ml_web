# Machine Learning Python Web Service 
python_web is a sample python web service for machine learning.

## Build 

```shell script

    docker build -t python_web -f Dockerfile . 

    docker run -it --rm \
                    -p  8020:8020 \
                    -e WORKERS=2 \
                    python_web

```