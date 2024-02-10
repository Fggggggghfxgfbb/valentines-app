import base64
from datetime import datetime
from flask import Flask, render_template, url_for, redirect, request
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators, TextAreaField, HiddenField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt
import os
import random
from multiprocessing import Value

count = Value('i', 1)
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'


class nameform(FlaskForm):
    name = StringField(validators=[InputRequired(), Length(min=4, max=20)],
                       render_kw={"placeholder": "Whats your name?"})
    submit = SubmitField("Confirm")


@app.route("/", methods=['GET', 'POST'])
def name():
    count.value = 1
    form = nameform()
    if form.validate_on_submit():
        return redirect(url_for('index', name1=form.name.data))
    return render_template("name.html", form=form)


@app.route("/<name1>", methods=['GET', 'POST'])
def index(name1):
    r = 13
    b = 1
    blub = 0.2

    if request.method == 'POST':
        if 'yes' in request.form:
            return redirect(url_for('index1', name1=name1))

        elif 'no' in request.form:
            r = random.randint(1, 24)
            b = random.randint(1, 4)
            count.value += 1
            blub = count.value / 5

    return render_template('home.html', blub=blub, text=b, multiplier=count.value, random=r, name1=name1)


@app.route("/<name1>/yayyyyy", methods=['GET', 'POST'])
def index1(name1):
    r = 13
    b = 1
    blub = 0.2
    count.value = 1

    return render_template('home2.html', blub=blub, text=b, multiplier=count.value, random=r, name1=name1)


app.run(debug=True, port=8000)
