from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        { 
            'author': {'username': 'John'},
            'body': 'Beautiful day in Bengaluru!'
        },
        { 
            'author': {'username': 'Susan'},
            'body': 'The Kantara movie was cool'
        }
    ]


    return render_template('index.html', title='Home', user=user, posts=posts)