from flask import Flask, render_template, request
from wtforms import StringField, PasswordField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'any secret string'


class SignupForm(FlaskForm):
    name = StringField("first name", validators=[InputRequired()])
    last = StringField("last name", validators=[InputRequired()])
    email = StringField("E-mail", [InputRequired("Please enter your E-mail address."), Email("Please enter your E-mail again.")])
    username = StringField("username", validators=[InputRequired()])
    password = PasswordField("password", validators=[InputRequired(), Length(min=8, message="Please enter at least 8 characters")])


@app.route('/')
def member():
    form = SignupForm()
    return render_template('signup.html', form=form)


@app.route('/register', methods=["GET", "POST"])
def register():
    form = SignupForm()
    if form.validate_on_submit():
        return "You are already registered."
    return render_template('signup.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)