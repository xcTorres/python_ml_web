#!/usr/bin/env bash

if [[ -z ${APP_DIR} ]]; then APP_DIR=.; fi
LOG_CONFIG_FILE=$APP_DIR/configs/logging.conf

gunicorn --log-config $LOG_CONFIG_FILE \
         -c ${APP_DIR}/gunicorn/gunicorn_conf.py \
         --preload \
         web_app.models:app
