from flask import Blueprint, render_template

app = Blueprint('branch', __name__)


@app.route('/branch/home')
def branch_home():
    return render_template('BM_dashboard.html', **locals())