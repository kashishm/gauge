import json
import os

from flask import Flask
from flask import make_response
from flask import request

from firebase import fb
from response.response import get_response

app = Flask(__name__)

fb.init()


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    print(json.dumps(req, indent=4))

    res = get_response(req)

    r = make_response(json.dumps(res.json, indent=4))
    r.headers['Content-Type'] = 'application/json'
    return r


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=False, port=port, host='0.0.0.0')
