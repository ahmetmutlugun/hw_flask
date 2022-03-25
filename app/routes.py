from flask import Flask, render_template, flash, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

myobj = Flask(__name__)
name = "Lisa"
city_names = ['Paris', 'London', 'Rome', 'Tahiti']

myobj.config.from_mapping(
    SECRET_KEY="Secret-Key")


class CityForm(FlaskForm):
    city_name = StringField('City Name', validators=[DataRequired()])
    submit = SubmitField('Submit')


@myobj.route("/")
def home():
    form = CityForm()
    print("Hello")
    if form.validate_on_submit():
        flash('Hello World'.format(form.city_name.data))
        print("Hello2")
        return redirect('/')
    return render_template("home.html", name=name, cities=city_names, form=form)