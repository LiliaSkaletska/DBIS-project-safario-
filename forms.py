from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class ContactForm(FlaskForm):
    message = StringField("message: ")
    customer_name = StringField("customer_name: ")
    age = StringField("age: ")
    email = StringField("email: ")
    submit = SubmitField("Submit")
