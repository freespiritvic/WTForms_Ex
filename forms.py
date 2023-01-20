from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, Length

class AddPetForm(FlaskForm):
    """Adding a pet form"""
    
    name = StringField('Pet Name',  
        validators=[InputRequired(message='Pet Name cannot be blank')])
    
    species = SelectField("Species", 
        choices=[('cat', 'Cat'), ('dog', 'Dog'), ('fish', 'Fish'), ('bird', 'Bird'), ('hamster', 'Hamster'), ('snake', 'Snake'), ('turtle', 'Turtle'), ('rabbit', 'Rabbit')])
    
    photo_url = StringField('Photo URL', 
        validators=[Optional(), URL()])
    
    age = IntegerField('Age', 
        validators=[Optional(), NumberRange(min=0, max=45)])
    
    notes = TextAreaField('Notes', 
        validators=[Optional(), Length(max=200)])

class EditPetForm(FlaskForm):
    """Editing a pet form"""

    photo_url = StringField('Photo URL',
        validators=[Optional(), URL()],)

    notes = TextAreaField('Notes',
        validators=[Optional(), Length(max=200)])

    available = BooleanField("Available?")