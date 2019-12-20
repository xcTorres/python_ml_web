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

RUN mkdir -p ${APP_DIR}/log
RUN mkdir -p /var/log/supervisor


# chmod all gunicorn
RUN chmod +x ./gunicorn/gunicorn-start.sh && \
    chmod +x ./gunicorn/supervisor.conf

ENTRYPOINT ["/usr/local/bin/supervisord", "-c", "./gunicorn/supervisord.conf"]

