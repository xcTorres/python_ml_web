# @Time    : 20/12/19 16:24
# @Author  :  xcTorres
# @FileName: __init__.py

from flask import Flask

app = Flask(__name__)

from web_app.views import house_pricing
app.register_blueprint(blueprint=house_pricing.house_pricing_blueprint)
