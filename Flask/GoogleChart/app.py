# https://www.roytuts.com/google-pie-chart-using-python-flask/

from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/google-charts/line-chart')
def google_line_chart():
    data = {
        '2006' : 1000,
        '2007' : 1050,
        '2008' : 900,
        '2009' : 1170
        }
    return render_template('line-chart.html', data=data)

@app.route('/google-charts/pie-chart')
def google_pie_chart():
    data = {'Task' : 'Hours per Day', 'Work' : 11, 'Eat' : 2, 'Commute' : 2, 'Watching TV' : 2, 'Sleeping' : 7}
    return render_template('pie-chart.html', data=data)

if __name__ == "__main__":
    app.run(port=8080)