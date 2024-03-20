from flask_wtf import FlaskForm  # Importing the FlaskForm class
from wtforms import StringField, TextAreaField, RadioField, SubmitField  # Importing form fields
from wtforms.validators import InputRequired, Email  # Importing validators

class DataCollectionForm(FlaskForm):
    # Defining form fields with labels and validators
    name = StringField('Name:', validators=[InputRequired()])  # Text field for name
    student_number = StringField('Student Number:', validators=[InputRequired()])  # Text field for student number
    email = StringField('Email Address:', validators=[InputRequired(), Email()])  # Text field for email
    grades = StringField('Grades obtained in courses:')  # Text field for grades
    # Radio field for overall satisfaction with academic experience
    satisfaction = RadioField('Overall satisfaction with the academic experience:',
                              choices=[('Very Dissatisfied', 'Very Dissatisfied'),  # Radio choices
                                       ('Dissatisfied', 'Dissatisfied'),
                                       ('Neutral', 'Neutral'),
                                       ('Satisfied', 'Satisfied'),
                                       ('Very Satisfied', 'Very Satisfied')])
    improvement = TextAreaField('Suggestions for improvement:')  # Text area for improvement suggestions
    submit = SubmitField('Submit')  # Submit button
