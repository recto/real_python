"""
Flask Task Controller
"""
from functools import wraps

from flask import Flask, flash, redirect, render_template, \
        request, session, url_for, g
from flask_sqlalchemy import SQLAlchemy
from forms import AddTaskForm

# config
app = Flask(__name__)
app.config.from_object('_config')
db = SQLAlchemy(app)

from models import Task

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
    flash('Goodbye')
    return redirect(url_for('login'))

@app.route('/', methods=['GET', 'POST'])
def login():
    """ return login page """
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] \
                or request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid Credentials. Please try again.'
            return render_template('login.html', error=error)
        else:
            session['logged_in'] = True
            flash('Welcome')
            return redirect(url_for('tasks'))
    return render_template('login.html')

@app.route('/tasks/')
@login_required
def tasks():
    """
    Return task.html with open tasks and closed tasks.
    """
    open_tasks = Task.query.filter_by(status='1').order_by(Task.due_date.asc())
    closed_tasks = Task.query.filter_by(status='0').order_by(Task.due_date.asc())
    return render_template(
        'tasks.html',
        form=AddTaskForm(request.form),
        open_tasks=open_tasks,
        closed_tasks=closed_tasks
    )

@app.route('/add/', methods=['POST'])
@login_required
def new_task():
    """
    Create new task.
    """
    form = AddTaskForm(request.form)
    if form.validate_on_submit():
        new_task = Task(
            form.name.data,
            form.due_date.data,
            form.priority.data,
            '1'
        )
        db.session.add(new_task)
        db.session.commit()
        flash('New entry was successfully posted. Thanks.')
        return redirect(url_for('tasks'))
    return redirect(url_for('tasks'))

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
