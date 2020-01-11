from flask import Blueprint, render_template

app = Blueprint('admin', __name__)


@app.route('/admin/home')
def admin_home(data = None):
    return render_template('admin/admin_home.html')

@app.route('/admin/add-new-employee', methods=['POST', 'GET'])
def add_employee():
    print('Adding Employee')
    return render_template('admin/admin_home.html')

@app.route('/admin/add-new-branch', methods=['POST', 'GET'])
def add_branch():
    print('Adding Branch')
    return render_template('admin/add_branch.html')

@app.route('/admin/assign-employee', methods=['POST', 'GET'])
def assign_employee():
    print('Assigning Roles')
    return render_template('admin/assign_role.html')

@app.route('/admin/all-employee', methods=['POST', 'GET'])
def view_all_emp():
    # pass
    return render_template('admin/all_employee.html')

@app.route('/admin/all-branch', methods=['POST', 'GET'])
def view_all_branch():
    # pass
    return render_template('admin/all_branch.html')
