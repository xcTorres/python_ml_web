From python:3.7.5-slim-stretch

RUN apt-get update \
    && apt-get install -y curl lsof procps g++

ENV APP_DIR /app_root
RUN mkdir -p ${APP_DIR}
WORKDIR ${APP_DIR}

# Install python library
RUN pip install --upgrade pip
ADD ./requirements.txt ${APP_DIR}
RUN pip install -r requirements.txt

COPY ./web_app ${APP_DIR}/web_app
COPY ./config  ${APP_DIR}/config
COPY ./algo ${APP_DIR}/algo
COPY ./tests ${APP_DIR}/tests
COPY ./gunicorn ${APP_DIR}/gunicorn
COPY ./worker ${APP_DIR}/worker


RUN mkdir -p ${APP_DIR}/log
RUN mkdir -p /var/log/supervisor
RUN mkdir -p /var/log/algo
RUN mkdir -p /var/log/worker

# chmod all gunicorn
RUN chmod +x ./gunicorn/gunicorn-start.sh && \
    chmod +x ./gunicorn/supervisord.conf && \
    chmod +x ./worker/worker-start.sh

#ENTRYPOINT ["/usr/local/bin/supervisord", "-c", "./gunicorn/supervisor.conf"]
