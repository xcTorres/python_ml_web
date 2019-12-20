# @Time    : 20/12/19 16:24
# @Author  :  xcTorres
# @FileName: __init__.py

from flask import Flask

app = Flask(__name__)

from web_app.views import hello_world
app.register_blueprint(blueprint=hello_world.hello_world_blueprint)
