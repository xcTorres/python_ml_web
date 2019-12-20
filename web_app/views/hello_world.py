# @Time    : 20/12/19 16:30
# @Author  :  xcTorres
# @FileName: hello_world.py


from flask import request, Blueprint, jsonify
from algo import logger

hello_world_blueprint = Blueprint('hello_world', __name__)


@hello_world_blueprint.route('/hello')
def hello():

    try:
        name = request.args.get('name', 'no one')
        logger.info(name)
        return jsonify({'hello world': name}), 200
    except Exception as e:
        logger.error(e)
        return jsonify({'msg': str(e), 'exception': type(e).__name__}), 500

