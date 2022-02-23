import json
import datetime
from flask import Flask
from flask_cors import CORS
from flask import request
import os


app = Flask("piomat-v2-server")
CORS(app)

# * requests

@app.route('/')
def test():
    # test
    return "hello world"


@app.route('/backup')
def backup():
    # backup
    data = request.get_json(force=True)
    cur_time = datetime.datetime.now()
    filename = cur_time.strftime("%Y_%m_%d_%H_%M_%S")
    os.makedirs("backups", exist_ok = True)
    with open("backups/" + filename + ".json", "w") as f: 
        json.dump(data, f)
    return ("", 204)

if __name__ == '__main__':
    # create backups folder if not present yet
    app.run(host="0.0.0.0", port=5090, threaded=False)
