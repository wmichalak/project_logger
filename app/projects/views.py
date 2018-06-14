# app/projects/views.py

from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from . import projects
from forms import EntryForm
from .. import db
from ..models import Project

@projects.route('/projects', methods=['GET', 'POST'])
@login_required
def register():
    """
    Handle requests to the /register route
    Add an project to the database through the registration form
    """
    form = EntryForm()
    if form.validate_on_submit():
        project = Project(employee=form.employee.data,
                          department = form.department.data,
                          document_type = form.document_type.data,
                          description = form.description.data,
                          data = form.date.data)

        # add project to the database
        db.session.add(project)
        db.session.commit()
        flash('You have successfully submitted project.')

        # redirect to the dashboard page
        return redirect(url_for('home.dashboard'))

    # load projects template
    return render_template('projects/projects.html', form=form, title='Project Document Submission')

