# app/home/views.py

from flask import abort, render_template, request
from flask_login import current_user, login_required

from . import home
from ..models import Project

@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('home/index.html', title="Siluria Technologies")

@home.route('/dashboard/<orderby>')
@login_required
def dashboard(orderby = None):
    """
    Render the dashboard template on the /dashboard route
    """
    print orderby
    if orderby == 'date':
        projects = Project.query.order_by(Project.date.desc()) #all()
    elif orderby == 'ID':
        projects = Project.query.all()
    elif orderby == 'project_name':
        projects = Project.query.order_by(Project.doc_name)
    elif orderby == 'owner':
        projects = Project.query.order_by(Project.employee)
    elif orderby == 'document':
        projects = Project.query.order_by(Project.document_type)


    return render_template('home/dashboard.html', projects=projects, title="Dashboard")

@home.route('/admin/dashboard')
@login_required
def admin_dashboard():
    # prevent non-admins from accessing the page
    if not current_user.is_admin:
        abort(403)
    projects = Project.query.all()
    return render_template('home/admin_dashboard.html', projects=projects, title="Dashboard")