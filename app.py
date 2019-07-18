from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', **locals())


@app.route('/services')
def services():
    return render_template('index.html', **locals())


@app.route('/latest-updates')
def latest_updates():
    return render_template('index.html', **locals())


@app.route('/recent-reports')
def recent_reports():
    return render_template('index.html', **locals())


@app.route('/my-team')
def my_team():
    return render_template('index.html', **locals())


@app.route('/about')
def about():
    return render_template('index.html', **locals())


if __name__ == '__main__':
    app.run()
