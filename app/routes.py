from flask import Flask, render_template, flash, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from app import myobj

name = "Lisa"
city_names = ['Paris', 'London', 'Rome', 'Tahiti']

myobj.config.from_mapping(
    SECRET_KEY="Secret-Key")


class CityForm(FlaskForm):
    city_name = StringField('City Name', validators=[DataRequired()])
    submit = SubmitField('Submit')


@myobj.route("/", methods=["GET", "POST"])
def home():
    form = CityForm()
    if form.validate_on_submit():
        flash('{}'.format(form.city_name.data))
        return redirect('/')
    return render_template("home.html", name=name, cities=city_names, form=form)
