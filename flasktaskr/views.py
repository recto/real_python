"""
Flask Task Controller
"""

from forms import AddTaskForm, RegisterForm, LoginForm
from functools import wraps
from flask import Flask, flash, redirect, render_template, \
        request, session, url_for, g
from flask_sqlalchemy import SQLAlchemy
import datetime



# config
app = Flask(__name__)
app.config.from_object('_config')
db = SQLAlchemy(app)

from models import Task, User

# helper functions
def login_required(test):
    """ check if user logged in. """
    @wraps(test)
    def wrap(*args, **kwargs):
        """ wrapper """
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

# route handlers
@app.route('/logout/')
def logout():
    """ logout """
    session.pop('logged_in', None)
    session.pop('user_id', None)
    flash('Goodbye')
    return redirect(url_for('login'))

@app.route('/', methods=['GET', 'POST'])
def login():
    """ return login page """
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(name=request.form['name']).first()
            if user is not None and user.password == request.form['password']:
                session['logged_in'] = True
                session['user_id'] = user.id
                flash('Welcome')
                return redirect(url_for('tasks'))
            else:
                error = 'Invalid username or password.'
        else:
            error = 'Both Fields are required.'
    return render_template('login.html', form=form, error=error)

@app.route('/tasks/')
@login_required
def tasks():
    """
    Return task.html with open tasks and closed tasks.
    """
    return render_template(
        'tasks.html',
        form=AddTaskForm(request.form),
        open_tasks=open_tasks(),
        closed_tasks=closed_tasks()
    )

@app.route('/add/', methods=['POST', 'GET'])
@login_required
def new_task():
    """
    Create new task.
    """
    error = None
    form = AddTaskForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            new_task = Task(
                form.name.data,
                form.due_date.data,
                form.priority.data,
                datetime.datetime.utcnow(),
                '1',
                session['user_id']
            )
            db.session.add(new_task)
            db.session.commit()
            flash('New entry was successfully posted. Thanks.')
            return redirect(url_for('tasks'))
        else:
            return render_template('tasks.html', form=form, error=error)
    return render_template('tasks.html', form=form, error=error,
            open_tasks=open_tasks(), closed_tasks=closed_tasks())

@app.route('/complete/<int:task_id>/')
@login_required
def complete(task_id):
    """
    Update the task and set its status to complete.
    """
    new_id = task_id
    Task.query.filter_by(task_id=new_id).update({"status": "0"})
    db.session.commit()
    flash('The task was marked as complete.')
    return redirect(url_for('tasks'))

@app.route('/delete/<int:task_id>/')
@login_required
def delete_entry(task_id):
    """
    Delete the task.
    """
    new_id = task_id
    Task.query.filter_by(task_id=new_id).delete()
    db.session.commit()
    flash('The task was deleted.')
    return redirect(url_for('tasks'))

@app.route('/register/', methods=['GET', 'POST'])
def register():
    """
    Register user.
    """
    error = None
    form = RegisterForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            new_user = User(
                form.name.data,
                form.email.data,
                form.password.data,
            )
            db.session.add(new_user)
            db.session.commit()
            flash('Thanks for registering. Please login.')
            return redirect(url_for('login'))
    return render_template('register.html', form=form, error=error)

def open_tasks():
    """
    return open tasks
    """
    return db.session.query(Task).filter_by(status='1').order_by(Task.due_date.asc())

def closed_tasks():
    """
    return closed tasks
    """
    return db.session.query(Task).filter_by(status='0').order_by(Task.due_date.asc())

def flash_errors(form):
    """
    flash errors
    """
    for field, erros in form.errors.items():
        for error in erros:
            flash("Error in the {0} field - {1}".format(
                getattr(form, field).label.text, error), 'error')
