import os

from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from forms import FeedbackForm

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# csrf config
app.config['SECRET_KEY'] = 'secret key'

# database config
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    form = FeedbackForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['content'] = form.content.data
        flash('You have submitted your feedback')
        return redirect(url_for('feedback'))
    return render_template(
        'feedback.html',
        form=form
    )


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.errorhandler(404)
def page_not_found(error):
    return render_template(
        'error.html', message=error, code=404
    ), 404


if __name__ == '__main__':
    app.run()
