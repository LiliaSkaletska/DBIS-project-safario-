from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, TextAreaField


class ContactForm(FlaskForm):
    message = StringField("message: ")
    customer_name = StringField("customer_name: ")
    age = IntegerField("age: ")
    email = StringField("email: ")
    tour_name = StringField("tour_name: ")
    submit = SubmitField("Submit")


class Feedback(FlaskForm):
    tour_name = StringField("tour_name: ")
    group_name = StringField("group_name: ")
    feedback_message = TextAreaField("feedback_message: ")
    submit = SubmitField("OK")
