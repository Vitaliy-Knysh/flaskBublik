from flask import Flask, render_template, url_for
app = Flask(__name__)
from flask import jsonify, request, render_template
import plotly.express as px
import time




@app.route('/')
def hello():
    return render_template('index.html')

if __name__ == '__main__':
    '''app.debug = True
    app.run()'''
    data = {'Task': ['Work', 'Eat', 'Commute', 'Watching TV', 'Sleeping'], 'Hours': [11, 2, 2, 2, 7]}
    fig = px.pie(data, names='Task', values='Hours', color_discrete_sequence=['blue'])
    fig.update_layout(paper_bgcolor='rgba(0, 255, 0, 0)',
                      plot_bgcolor='rgba(255, 0, 0, 0)',
                      font_color='black',
                      font_family='verdana',
                      font_size=20)
    fig.show()
    fig.write_html('test.html')
    time.sleep(3)