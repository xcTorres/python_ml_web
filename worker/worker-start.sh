#!/bin/sh

celery multi start 5 -A worker.worker -c 1 -O fair -l info