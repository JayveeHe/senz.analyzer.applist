# -*- encoding:utf-8 -*-
__author__ = 'zhongziyuan'

from flask import Flask, request
from static_info import InfoGetter
import json

app = Flask(__name__)

@app.route("/static_info", methods=['GET'])
def get_static_info():
    if request.method == 'GET':
        apps = request.args.get('app_list')
        if not apps:
            return '{"error":"param error:no app_list"}'

        i = InfoGetter()
        return json.dumps(i.get_labels(apps.split(',')))

    return "Please use GET!"

if __name__ == "__main__":
    app.debug = True
    app.run(port=8080)