from flask import Flask, render_template, url_for

app = Flask(__name__)
from flask import jsonify, request, render_template
import time
from threading import Thread
from elasticsearch import Elasticsearch

'''@app.route('/')
def hello():
    return render_template('sunburst-chart.html', numbers=[88, 84, 77, 66, 55, 50, 34],
                           names=['1', '2', '3', '4', '5', '6', '7'])'''

val = [10, 14, 4, 6, 10, 4]

@app.route('/')
def hello():
    return render_template('sunburst-chart.html',
                           ids=["Шуя", "Тверь", "Шуя - PASS", "Шуя - FAIL", "Тверь - PASS", "Тверь - FAIL"],
                           labels=["Шуя", "Тверь", "PASS " + '<br>' + str(round(100 * (val[2] / val[0]))) + '%',
                                   "FAIL" + '<br>' + (str(round(100 * val[3] / val[0]))) + '%',
                                   "PASS" + '<br>' + (str(round(100 * val[4] / val[1]))) + '%',
                                   "FAIL" + '<br>' + (str(round(100 * val[5] / val[1]))) + '%'],
                           parents=["", "", "Шуя", "Шуя", "Тверь", "Тверь"],
                           values=val)


if __name__ == '__main__':
    # es = Elasticsearch(address="172.26.24.198", port="9200", login="elastic", password="1qazXSW@")
    # print(es.ping())
    # new_thread.start()
    app.run(debug=True)
