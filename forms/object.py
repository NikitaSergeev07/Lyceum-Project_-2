from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms import  SubmitField, FloatField
from wtforms.validators import DataRequired

class ObjectForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])
    content = TextAreaField("Содержание")
    price = FloatField('Цена')
    submit = SubmitField('Применить')