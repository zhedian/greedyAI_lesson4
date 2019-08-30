from flask import Flask
import requests

app = Flask(__name__)


@app.route('/<data>')
def hello_world(data):
    if "帅" in data:
        return "唐僧"
    elif "好看" in data:
        return "白骨精"
    else:
        data_param = {
            "reqType": 0,
            "perception": {
                "inputText": {
                    "text": data
                }
            },
            "userInfo": {
                "apiKey": "28dc7687f5c3486a87c46b469f9f1593",
                "userId": "038122881ee5117c"
            }
        }
        response = requests.post(url='http://openapi.tuling123.com/openapi/api/v2', json=data_param)
        return response.text
if __name__ == '__main__':
    app.run()

