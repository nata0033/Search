import os
import json
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)
filename = os.path.join(app.static_folder, '', 'data.json')
with open(filename) as json_file:
    data = json.load(json_file)


@app.route("/")
def index():
    return render_template('index.html')


def in_beginning(w1, w2):
    min_size = len(w1)
    if len(w2) < min_size:
        min_size = len(w2)
    for i in range(0, min_size):
        if w1[i] != w2[i]:
            return False
    return True


@app.route("/search", methods=['GET', 'POST'])
def search():
    all_words = data['data']
    selected_words = {"data": []}
    if request.method == 'POST':
        q = json.loads(request.get_json())['input_value']
        if q:
            for word in all_words:
                #if q.lower() in word.lower():
                if in_beginning(q.lower(), word.lower()):
                    selected_words["data"].append(word)
            return jsonify(selected_words)
    return jsonify(selected_words)


if __name__ == "__main__":
    app.run(debug=True)
