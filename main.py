import redis
from flask import Flask, request, abort


app = Flask(__name__)
r = redis.Redis(host='0.0.0.0', port=6379)


@app.route('/<key>', methods=['GET'])
def get(key):
    value = r.get(key)
    if value == None:
        abort(404)
    return value


@app.route('/', methods=['POST'])
def post():
    dct = request.get_json()
    key = list(dct.keys())[0]
    value = dct.get(key)
    r.set(key, value)
    return 'OK'
    

@app.route('/<key>', methods=['PUT'])
def put(key):
    if r.get(key) == None:
        abort(404)
    value = request.get_json().get(key)
    r.set(key, value)
    return 'OK'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

