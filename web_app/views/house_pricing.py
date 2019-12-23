# @Time    : 20/12/19 16:30
# @Author  :  xcTorres
# @FileName: house_pricing.py

import numpy as np
from flask import request, Blueprint, jsonify, Response
from algo import logger
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

    try:
        model = request.environ['HTTP_MODEL']
        feature = [3.6135235573122535, 11.363636363636363, 11.136778656126504, 0.0691699604743083, 0.5546950592885372,
                                          6.284634387351787, 68.57490118577078, 3.795042687747034, 9.549407114624506, 408.2371541501976,
                                          18.455533596837967, 356.67403162055257, 12.653063241106723]
        x = np.asarray([feature], dtype=np.float32)
        y = model.predict(x)
        return jsonify({'price': y[0]}), 200
    except Exception as e:
        logger.error(e)
        return jsonify({'msg': str(e), 'exception': type(e).__name__}), 500


@house_pricing_blueprint.route("/metrics")
def metrics():
    registry = CollectorRegistry()
    multiprocess.MultiProcessCollector(registry)
    data = generate_latest(registry)
    return Response(data, mimetype=CONTENT_TYPE_LATEST)