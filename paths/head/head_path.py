from flask import Blueprint, render_template

app = Blueprint('head', __name__)

@app.route('/head/home')
def head_home():
    return render_template('HO_dashboard.html', **locals())