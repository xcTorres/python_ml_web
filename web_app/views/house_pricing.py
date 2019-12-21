# @Time    : 20/12/19 16:30
# @Author  :  xcTorres
# @FileName: house_pricing.py

import numpy as np
from flask import request, Blueprint, jsonify
from algo import logger

house_pricing_blueprint = Blueprint('house_pricing', __name__)


@house_pricing_blueprint.route('/pricing')
def pricing():

    # model.predict([3.6135235573122535, 11.363636363636363, 11.136778656126504, 0.0691699604743083, 0.5546950592885372,
    #                6.284634387351787, 68.57490118577078, 3.795042687747034, 9.549407114624506, 408.2371541501976,
    #                18.455533596837967, 356.67403162055257, 12.653063241106723])
    model = request.environ['MODEL']
    feature = [3.6135235573122535, 11.363636363636363, 11.136778656126504, 0.0691699604743083, 0.5546950592885372,
                                      6.284634387351787, 68.57490118577078, 3.795042687747034, 9.549407114624506, 408.2371541501976,
                                      18.455533596837967, 356.67403162055257, 12.653063241106723]
    try:
        x = np.asarray([feature], dtype=np.float32)
        y = model.predict(x)
        return jsonify({'price': y[0]}), 200
    except Exception as e:
        logger.error(e)
        return jsonify({'msg': str(e), 'exception': type(e).__name__}), 500

    # try:
    #     name = request.args.get('name', 'no one')
    #     logger.info(name)
    #     return jsonify({'hello world': name}), 200
    # except Exception as e:
    #     logger.error(e)
    #     return jsonify({'msg': str(e), 'exception': type(e).__name__}), 500

