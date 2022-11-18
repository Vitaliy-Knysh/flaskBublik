from flask import Flask, render_template, url_for

app = Flask(__name__)
from flask import jsonify, request, render_template
import time
from threading import Thread


@app.route('/')
def hello():
    return render_template('pie-chart.html', numbers=[88, 84, 77, 66, 55, 50, 34],
                           names=['Укропу', 'Кошачью жопу', 'Картошек', 'Мандавошек', 'Воды', 'Хуёв туды', 'Дров'])


if __name__ == '__main__':
    # new_thread.start()
    app.debug = True
    app.run()
