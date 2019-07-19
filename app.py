from flask import Flask, render_template, request

from services import ReportGenerationS as RGS
from classes import ReportGenerationClass as RGC

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


@app.route('/report-generation')
def report_generation():
    report_id = RGS.report_generation()
    return render_template('report_generation.html', **locals())


@app.route('/report-generation-done', methods=['POST', 'GET'])
def report_generation_done():
    print(request.form)
    if request.method == "POST":
        data = request.form
        print(data)
    # report_id = RGS.report_generation()
    return render_template('report_share.html', **locals())


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', **locals())


@app.route('/Notifications')
def notifications():
    return render_template('notifications.html', **locals())


@app.route('/report-submit')
def report_submit():
    return render_template('report_submit.html', **locals())


@app.route('/report-submit-done', methods=['POST', 'GET'])
def report_submit_done():
    # if request.method=="POST":
    #     data = request.form
    return render_template('index.html', **locals())


@app.route('/responses-view', methods=['POST', 'GET'])
def response_view():
    return render_template('responses_view.html')


@app.route('/responses-analysis', methods=['POST', 'GET'])
def response_analysis():
    return render_template('responses_analysis.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    return render_template('login.html')

@app.route('/login-done', methods=['POST', 'GET'])
def login_submit_done():

    if request.method == "POST":
        data = request.form
        print(data)
        if data['role']=='zm':
            return render_template('login.html')
    return render_template('index.html', **locals())

if __name__ == '__main__':
    app.run()
