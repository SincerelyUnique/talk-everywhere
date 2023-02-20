import json

import requests
from flask import Flask, request, jsonify
import openai

app = Flask(__name__)


@app.route('/chat', methods=['POST'])
def hello_world():
    api_key = "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"
    openai.api_key = api_key
    # headers = {'Authorization': 'Bearer ' + api_key}
    # res = requests.get(url="https://api.openai.com/v1/models", headers=headers)
    # content = json.loads(res.content)
    # print(content)
    prompt = request.get_json()['questionText']
    model_engine = "text-davinci-003"
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    print(message)
    res = {
        'code': 200,
        'message': message
    }
    return jsonify(res)


if __name__ == '__main__':
    app.run()
