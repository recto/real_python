"""
Flask blog application
"""
import sqlite3
from flask import Flask, render_template, request, session, flash, \
        redirect, url_for, g
from functools import wraps

# configuration
DATABASE = 'blog.db'
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = 'hard_to_guess'

app = Flask(__name__)

# pulls in app configuration by looking for UPPERCASE variables
app.config.from_object(__name__)

def login_required(test):
    """ return wraps that checks if user logged in """
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

def connect_db():
    """function used for connecting to the database"""
    return sqlite3.connect(app.config['DATABASE'])

@app.route('/', methods = ['GET', 'POST'])
def login():
    """
    login
    """
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] or \
                request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid Credentials. Please try again!'
        else:
            session['logged_in'] = True
            return redirect(url_for('main'))

    return render_template('login.html', error=error)

@app.route('/main')
@login_required
def main():
    """
    return main page
    """
    g.db = connect_db()
    cur = g.db.execute('select * from posts')
    posts = [dict(title=row[0], post=row[1]) for row in cur.fetchall()]
    return render_template('main.html', posts=posts)

@app.route('/add', methods=['POST'])
@login_required
def add():
    """
    Add a post to the blog.
    """
    title = request.form['title']
    past = request.form['post']
    if not title or not post:
        flash("All fields are required. Please try again.")
    else:
        g.db = connect_db()
        cur = g.db.execute('insert into posts (title, post) values (?, ?)', 
                [title, post])
        g.db.commit()
        g.db.close()
        flash("New entry was successfully posted!")
        return redirect(url_for('main'))

@app.route('/logout')
def logout():
    """
    logout
    """
    session.pop('logged_in', None)
    flash('You were logged out.')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
