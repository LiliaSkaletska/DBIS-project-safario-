from flask import Flask, render_template, url_for, redirect, request
from forms import ContactForm, Feedback
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ORM_tables_creating import customer, feedback
import sqlalchemy

global current_page
current_page = "index"

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thecodex'

@app.route('/')
def index():
    global current_page
    current_page = "index"
    return render_template("index.html")

@app.route('/package/')
def package():
    global current_page
    current_page = "package"
    return render_template("package.html")

@app.route('/contact/', methods=['GET', 'POST'])
def contact():
    global current_page
    current_page = "contact"
    form = ContactForm()
    if form.is_submitted():
       # try:
            oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{host}:{port}/{sid}'

            engine = create_engine(oracle_connection_string.format(

                username="PROJECT",
                password="Oracle",
                sid="XE",
                host="localhost",
                port="1521",
                database="PROJECT",
            ), echo=True)

            Session = sessionmaker(bind=engine)
            session = Session()

            result = request.form
            adddata = customer(result['message'], result['customer_name'], result['age'], result['email'], result['tour_name'])
            session.add(adddata)
            session.commit()
            return render_template('contactsubmit.html', result=result)

       # except:
        #   result = request.form
         #  return render_template('submitfail.html', result=result)

    return render_template('contact.html', form=form)


@app.route('/feedback/', methods=["GET", "POST"])
def message():
    global current_page
    current_page = "feedback"
    form = Feedback()
    if form.is_submitted():
       # try:
            oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{host}:{port}/{sid}'
            engine = create_engine(oracle_connection_string.format(

                username="PROJECT",
                password="Oracle",
                sid="XE",
                host="localhost",
                port="1521",
                database="PROJECT",
            ), echo=True)

            Session = sessionmaker(bind=engine)
            session = Session()

            result = request.form
            adddata = feedback(result['tour_name'], result['group_name'], result['feedback_message'])
            session.add(adddata)
            session.commit()
            return render_template('contactsubmit.html', result=result)

       # except:
        #    result = request.form
         #   return render_template('submitfail.html', result=result)

    return render_template('feedback.html', form=form)

if __name__ == '__main__':
   app.run()