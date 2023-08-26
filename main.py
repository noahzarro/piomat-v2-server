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




@app.route('/backup', methods=['POST', 'GET'])
def backup():
    if request.method == 'GET':
        # get the names of all backup files
        backups = os.listdir("/mount/backups/")
        return {"backups": backups}
    if request.method == 'POST':    
        # save backup
        data = request.get_json(force=True)
        cur_time = datetime.datetime.now()
        filename = cur_time.strftime("%Y_%m_%d_%H_%M_%S")
        print("saving data:")
        print(data)
        os.makedirs("backups", exist_ok = True)
        with open("/mount/backups/" + filename + ".json", "w") as f: 
            json.dump(data, f)
        return ("", 204)

@app.route('/backup/<filename>', methods=['GET'])
def single_backup(filename):
    if request.method == 'GET':
        # get a single backup file
        backup = {}
        with open("/mount/backups/" + filename) as f:
            backup = json.load(f)
        return {"backup": backup}

if __name__ == '__main__':
    # create backups folder if not present yet
    app.run(host="0.0.0.0", port=5090, threaded=False)
