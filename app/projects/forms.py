# app/projects/forms.py

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, DateTimeField, SelectField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired
from datetime import datetime
from .. import db
from ..models import Employee, Department


class EntryForm(FlaskForm):
    """
    Form for users to submit project document into log
    """

    employee = StringField('employee', validators=[DataRequired()]) #QuerySelectField(query_factory=lambda: Employee.query.all(),get_label="name")
    department = StringField('department', validators=[DataRequired()]) #QuerySelectField(query_factory=lambda: Department.query.all(),get_label="name")
    document_type = SelectField('Document type', choices=[('SOW','Scope of work'),('IER','Individual Experiment Report'),
                                                          ('TPS','Technology Progress Summary'),('TES','Technology Evaluation Summary')])
    description = StringField('Description', validators=[DataRequired()])
    date = DateTimeField('Date',format="%Y-%m-%dT%H:%M:%S",
                         default=datetime.today,
                         validators=[DataRequired()])
    submit = SubmitField('Submit')




