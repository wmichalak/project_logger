# app/projects/forms.py

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, DateTimeField, SelectField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired
from datetime import datetime
from .. import db
from ..models import Employee, Department


class ProjectEntryForm(FlaskForm):
    """
    Form for users to submit project document into log
    """

    employee = QuerySelectField(query_factory=lambda: Employee.query.filter(Employee.is_admin == False),get_label="username", allow_blank=True)
    document_type = SelectField('Document type', choices=[('SOW','Scope of work'),('IER','Individual Experiment Report'),
                                                          ('TPS','Technology Progress Summary'),('TER','Technology Evaluation Report'),
                                                          ('TOS','Technology Opportunity Scoping')])
    name = StringField('Project name', validators=[DataRequired()])
    date = DateTimeField('Date',format="%Y_%m_%d",default=datetime.today,validators=[DataRequired()])
    submit = SubmitField('Submit')




