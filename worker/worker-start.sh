#!/bin/sh

celery multi start 5 -A worker.worker -l info