
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['DEBUG'] = True
app.config['JSON_SORT_KEYS'] = False

@app.route('/chat', methods=['GET','POST'])
def rasa():

    if request.method == 'POST':
        id = request.get_json()['id']
        msg = request.get_json()['msg']

        url = 'http://localhost:5005/webhooks/rest/webhook'

        data = {'sender':id, 'message':msg}

        result = requests.post(url=url, json = data)

        return jsonify(result.json())

if __name__ == "__main__":
    app.run()