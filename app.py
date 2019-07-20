from flask import Flask, render_template, request, redirect, session

from services import ReportGenerationS as RGS
from classes import ReportGenerationClass as RGC
from services import auth
app = Flask(__name__)
app.secret_key = "moonmuniakashob"


@app.route('/home')
def home():
    print(session['username'])
    return render_template('index.html', **locals())


@app.route('/')
def login(data=None):
    if 'username' in session.keys():
        return redirect('/home')
    return render_template('login.html', **locals())


@app.route('/validation-login-info', methods=['POST', 'GET'])
def validation_login_info():
    if request.method == 'POST':
        data = request.form
        flag, user = auth.validation(data)
        print(flag, user, ' printing from validation ')
        if flag == False:
            return redirect('/')
    session['username'] = user['username']
    return redirect('/')


@app.route("/logout")
def logout():
    if 'username' in session.keys():
        session.pop('username')
    return redirect('/')


@app.route('/register')
def register():
    return render_template('register.html', **locals())


@app.route('/save-register-info', methods=['POST', 'GET'])
def save_register_info():
    if request.method == 'POST':
        data = request.form
        auth.save_register_info(data)
    return redirect('/home')


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


@app.route('/report-generation-done/<report_id>', methods=['POST', 'GET'])
def report_generation_done(report_id):
    # print(request.form)
    if request.method == "POST":
        data = request.form
        RGS.add_questions(report_id, data)
    # report_id = RGS.report_generation()
    return render_template('report_share.html', **locals())


@app.route('/dashboard')
def dashboard():
    report_id = '5d32001e2ce6750a5b630230'
    report = RGS.get_report(report_id)
    report_list = []
    report_list.append([report_id, report['name']])
    return render_template('dashboard.html', **locals())


@app.route('/Notifications')
def notifications():
    return render_template('notifications.html', **locals())


@app.route('/report-submit')
def report_submit():
    report_id = '5d32001e2ce6750a5b630230'
    report = RGS.get_report(report_id)
    report_name = report['name']
    questions = report['questions']
    questions = dict(sorted(questions.items()))
    # print(questions, ' Here printing')
    keyList = []
    for key in sorted(questions):
        keyList.append(key)
    keyList = sorted(keyList)
    print(keyList)
    return render_template('report_submit.html', **locals())


@app.route('/report-submit-done/<report_id>', methods=['POST', 'GET'])
def report_submit_done(report_id):
    if request.method == 'POST':
        data = request.form
        response_id = RGS.save_reponseToDB(data)
        RGS.attached_responseID_to_reportID(report_id, response_id)
    return redirect('/')


@app.route('/responses-view/<report_id>', methods=['POST', 'GET'])
def response_view(report_id):
    return render_template('responses_view.html', **locals())


@app.route('/responses-analysis/<report_id>', methods=['POST', 'GET'])
def response_analysis(report_id):
    return render_template('response_analysis_categories.html', **locals())


@app.route('/responses-analysis-summarization/<report_id>', methods=['POST', 'GET'])
def response_analysis_summarization(report_id):
    return render_template('responses_analysis.html', **locals())


@app.route('/data-analysis', methods=['POST', 'GET'])
def data_analysis():
    return render_template('analysis_categories.html')


@app.route('/correlation-graph', methods=['POST', 'GET'])
def correlation_graph():
    return render_template('correlation_graph.html', **locals())


@app.route('/trend-analysis', methods=['POST', 'GET'])
def trend_analysis():
    return render_template('trend_analysis.html', **locals())


@app.route('/prediction', methods=['POST', 'GET'])
def prediction():
    return render_template('predictions.html', **locals())


@app.route('/send-report-done/<report_id>', methods=['POST', 'GET'])
def send_report_done(report_id):
    print(report_id, ' : sent_reportId')
    return redirect('/home')


@app.route('/correlation-graph-category')
def correlation_graph_category():
    # print(report_id, ' : sent_reportId')
    report_id = None
    return render_template('correlation_graph_categories.html', **locals())


@app.route('/analysis-correlation-graph-category')
def analysis_correlation_graph_category():
    # print(report_id, ' : sent_reportId')
    return render_template('analysis_correlation_graph_category.html')



@app.route('/t', methods=['POST', 'GET'])
def test():
    return render_template('test.html')

if __name__ == '__main__':
    app.run()