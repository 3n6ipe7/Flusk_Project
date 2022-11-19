from flask import Flask, url_for, render_template, redirect

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Secret_secret_key'

@app.route("/image")
def image():
    return f'''<img src="{url_for('static', filename='img/what.png')}"
           alt="здесь должна была быть картинка, но не нашлась">'''



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)



@app.route('/sample_page')
def return_sample_page():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет!?</title>
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" /> 
                  </head>
                  <body>
                    <h1>Первая HTML-страница</h1>
                    <img src="{url_for('static', filename='img/what.png')}"
           alt="здесь должна была быть картинка, но не нашлась">
                  </body>
                </html>"""


if __name__ == "__main__":
    app.run()
