"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from ResumeWebAppFlask import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page'
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/resume')
def resume():
    """Renders the about page."""
    return render_template(
        'resumehome.html',
        title='Resume',
        year=datetime.now().year,
        message='Resume Home',
    )

@app.route('/experience')
def experience():
    """Renders the about page."""
    return render_template(
        'resume_experience.html',
        title='Experience',
        year=datetime.now().year,
        message='Resume Home',
    )

@app.route('/education')
def education():
    """Renders the about page."""
    return render_template(
        'resume_education.html',
        title='Education',
        year=datetime.now().year,
        message='Resume Home',
    )

@app.route('/skills')
def skills():
    """Renders the about page."""
    return render_template(
        'resume_skills.html',
        title='Skills',
        year=datetime.now().year,
        message='Resume Home',
    )

@app.route('/interests')
def interests():
    """Renders the about page."""
    return render_template(
        'resume_interests.html',
        title='Interests',
        year=datetime.now().year,
        message='Resume Home',
    )

@app.route('/awards')
def awards():
    """Renders the about page."""
    return render_template(
        'resume_awards.html',
        title='AWARDS & HONOR SOCIETIES',
        year=datetime.now().year,
        message='Resume Home',
    )