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

val_left = [10, 14, 4, 6, 10, 4]
test_dict = {'family-1': [4, 7],
             'family-2': [1, 12],
             'family-3': [9, 9],
             'family-4': [3, 10]
             }

val_right = []
colors = []
parents_r = []
ids_r = list(test_dict.keys())
labels_r = list(test_dict.keys())
colors_r = []

for i in test_dict:
    val_right.append(test_dict[i][0] + test_dict[i][1])
    parents_r.append("")
    colors_r.append("#17a2b8")  # light blue

for i in test_dict:
    val_right.append(test_dict[i][0])
    val_right.append(test_dict[i][1])

for i in test_dict.keys():
    ids_r.append(i + ' - FAIL')
    ids_r.append(i + ' - PASS')
    labels_r.append(i + ' not ready: ' + str(test_dict[i][0]))
    labels_r.append(i + ' ready: ' + str(test_dict[i][1]))
    parents_r.append(i)
    parents_r.append(i)
    colors_r.append('red')
    colors_r.append('green')
print(colors_r)


@app.route('/')
def hello():
    return render_template('sunburst-chart.html',
                           ids_left=["Шуя", "Тверь", "Шуя - PASS", "Шуя - FAIL", "Тверь - PASS", "Тверь - FAIL"],
                           labels_left=["Шуя", "Тверь", "PASS " + '<br>' +
                                        str(round(100 * (val_left[2] / val_left[0]))) + '%',
                                        "FAIL" + '<br>' + (str(round(100 * val_left[3] / val_left[0]))) + '%',
                                        "PASS" + '<br>' + (str(round(100 * val_left[4] / val_left[1]))) + '%',
                                        "FAIL" + '<br>' + (str(round(100 * val_left[5] / val_left[1]))) + '%'],
                           parents_left=["", "", "Шуя", "Шуя", "Тверь", "Тверь"],
                           values_left=val_left,

                           # ids_right=["Шуя", "Тверь", "Шуя - PASS", "Шуя - FAIL", "Тверь - PASS", "Тверь - FAIL"],
                           # labels_right=["Шуя", "Тверь", "PASS " + '<br>' +
                           #               str(round(100 * (val_right[2] / val_right[0]))) + '%',
                           #               "FAIL" + '<br>' + (str(round(100 * val_right[3] / val_right[0]))) + '%',
                           #               "PASS" + '<br>' + (str(round(100 * val_right[4] / val_right[1]))) + '%',
                           #               "FAIL" + '<br>' + (str(round(100 * val_right[5] / val_right[1]))) + '%'],
                           # parents_right=["", "", "Шуя", "Шуя", "Тверь", "Тверь"],

                           ids_right=ids_r,
                           labels_right=labels_r,
                           parents_right=parents_r,
                           values_right=val_right,
                           colors_right=colors_r,

                           good_boards=1, bad_boards=1, all=1, good=1, bad=1)


if __name__ == '__main__':
    '''es = Elasticsearch(address="172.26.24.198", port="9200", login="elastic", password="1qazXSW@")
    print(es.ping())'''
    # new_thread.start()
    app.run(debug=True)
    '''for j in test_dict.keys():
        print(j)'''