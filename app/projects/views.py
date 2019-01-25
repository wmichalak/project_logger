# app/projects/views.py

from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from sqlalchemy import func

from . import projects
from forms import ProjectEntryForm
from .. import db
from _mysql_exceptions import IntegrityError
from ..models import Project, Employee


@projects.route('/projects', methods=['GET', 'POST'])
@login_required
def register():
    """
    Handle requests to the /register route
    Add a project to the database through the registration form
    """
    form = ProjectEntryForm()
    if form.validate_on_submit():

        # get total entries
        new_ID = str(len(Project.query.all())+1).zfill(4)

        department_dict = {'Development': 'DEV',
                           'Research': 'RES',
                           'Commercial Engineering': 'CE',
                           'Business Development': 'BIDEV'}

        department = department_dict[Employee.query.filter_by(username=form.employee.data.username).first().department.name]

        project = Project(name=form.name.data,
                          employee=form.employee.data.username,
                          document_type = form.document_type.data,
                          date = form.date.data,
                          doc_name = form.document_type.data + '_' + form.date.data.strftime("%Y%m%d") + '_' + department + '_' + new_ID + '.docx')

        # add project to the database
        db.session.add(project)

        try:
            db.session.commit()
            # redirect to the dashboard page
            return redirect(url_for('home.dashboard', orderby = 'date'))
        except:
            flash('You have entered a used project name. Please try a new name.')
    # load projects template
    return render_template('projects/projects.html', form=form, title='Project Document Submission')

