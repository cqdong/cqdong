from flask_wtf import Form
from flask_pagedown.fields import  PageDownField
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import Required

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')

class PostForm(Form):
    title = StringField('Title', validators=[Required()])
    body = TextAreaField("What's on your mind?", validators=[Required()])
    submit = SubmitField('Submit')