import redis
import os
from flask_redis import FlaskRedis
from flask_cors import CORS
from flask import Flask, request

app = Flask(__name__)
CORS(app)
app.config['REDIS_URL'] = os.environ['REDIS_URL']
r = FlaskRedis(app)

@app.route("/<path:path>", methods=['POST', 'GET'])
def hello(path):
    if request.method == 'POST':
        try:
            r.set(path, request.form['data'])
            r.expire(path, 3600 * 24 * 30 * 6)
            return ''
        except Exception as e:
            return e, 400

    if request.method == 'GET':
        v = r.get(path)
        if v is None:
            return '', 404
        r.expire(path, 3600 * 24 * 30 * 6)
        return v

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
