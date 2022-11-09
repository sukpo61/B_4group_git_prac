from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:go3355@cluster0.vqsgnyr.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/')
def main():
    return render_template('main.html')

@app.route('/GHS')
def go():
    return render_template('GHS.html')

@app.route('/CSH')
def mari():
    return render_template('CSH.html')


@app.route('/HJH')
def yee():
    return render_template('HJH.html')

@app.route('/NDH')
def kimm():
    return render_template('NDH.html')

@app.route('/YJH')
def kimw():
    return render_template('YJH.html')

@app.route("/comment", methods=["POST"])
def comment_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    person_receive = request.form['person_give']

    doc = {'name': name_receive,
           'comment': comment_receive,
           'person': person_receive}

    db.collection.insert_one(doc)

    return jsonify({'msg':'POST 연결 완료!'})

@app.route("/comment", methods=["GET"])
def comment_get():
    comment_list = list(db.collection.find({}, {'_id': False}))

    return jsonify({'comments': comment_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)


