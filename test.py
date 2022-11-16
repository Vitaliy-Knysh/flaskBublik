from flask import Flask, render_template, url_for
app = Flask(__name__)
from flask import jsonify, request, render_template

@app.route('/')
def hello():
    data = {'Task': 'Hours per Day', 'Work': 11, 'Eat': 2, 'Commute': 2, 'Watching TV': 2, 'Sleeping': 7}
    return render_template('pie-chart.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
