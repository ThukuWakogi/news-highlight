from flask import render_template
from . import main

@main.app_errorhandler(404)
def fourohfour(error):
  '''
  renders 404 page
  '''

  return render_template('404.html'), 404
