from flask import Flask, render_template

app = Flask(__name__)


@app.route('/map1_1')
def map1_1_page():
    return render_template('map_1_1.html')


@app.route('/map1_2')
def map1_2_page():
    return render_template('map_1_2.html')


@app.route('/map1_3')
def map1_3_page():
    return render_template('map_1_3.html')


@app.route('/map1_4')
def map1_4_page():
    return render_template('./data/map/map_1_4.html')


@app.route('/map1_5')
def map1_5_page():
    return render_template('map_1_5.html')


@app.route('/map1_6')
def map1_6_page():
    return render_template('map_1_6.html')


@app.route('/map1_7')
def map1_7_page():
    return render_template('map_1_7.html')


@app.route('/map1_8')
def map1_8_page():
    return render_template('map_1_8.html')


@app.route('/map1_9')
def map1_9_page():
    return render_template('map_1_9.html')


@app.route('/map1_10')
def map1_10_page():
    return render_template('map_1_10.html')


@app.route('/map1_10')
def map1_11_page():
    return render_template('map_1_11.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)