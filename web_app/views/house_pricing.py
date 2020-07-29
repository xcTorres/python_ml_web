# @Time    : 20/12/19 16:30
# @Author  :  xcTorres
# @FileName: house_pricing.py

import numpy as np
from flask import request, Blueprint, jsonify, Response
from algo import logger
from worker import worker
from prometheus_client import multiprocess
from prometheus_client import generate_latest, CollectorRegistry, CONTENT_TYPE_LATEST, Gauge, Summary

house_pricing_blueprint = Blueprint('house_pricing', __name__)

"""
    monitor metrics initialize
"""
IN_PROGRESS = Gauge("batch_assign_inprogress_requests", "batch assign inprogress requests number", multiprocess_mode='livesum')
REQUEST_LATENCY = Summary('batch_assign_request_latency', 'batch assign request latency')


@IN_PROGRESS.track_inprogress()
@REQUEST_LATENCY.time()
@house_pricing_blueprint.route('/pricing')
def pricing():

    if request.method == 'GET':
        crim = request.args.get('CRIM', 3.613)
        zn = request.args.get('ZN', 11.363)
        indus = request.args.get('INDUS', 11.137)
        chas = request.args.get('CHAS', 0.069)
        nox = request.args.get('NOX', 0.554)
        rm = request.args.get('RM', 6.284)
        age = request.args.get('AGE', 68.57)
        dis = request.args.get('DIS', 3.79)
        rad = request.args.get('RAD', 9.55)
        tax = request.args.get('TAX', 408.23)
        ptratio = request.args.get('PTRATIO', 18.45)
        b = request.args.get('B', 356.67)
        lstat = request.args.get('LSTAT', 12.653)
        feature = [crim, zn, indus, chas, nox, rm, age, dis, rad, tax, ptratio, b, lstat]
    try:
        x = np.asarray([feature], dtype=np.float32)
        t = worker.process.s({'x': x.tolist()}).apply_async()
        result = t.get()
        t.forget()
        logger.info({'price': result})
        return jsonify({'price': result}), 200
    except Exception as e:
        logger.error(e)
        return jsonify({'msg': str(e), 'exception': type(e).__name__}), 500


@house_pricing_blueprint.route("/metrics")
def metrics():
    registry = CollectorRegistry()
    multiprocess.MultiProcessCollector(registry)
    data = generate_latest(registry)
    return Response(data, mimetype=CONTENT_TYPE_LATEST)