from flask import render_template
from . import main
from ..requests import get_sources

#views
@main.route('/')
def index():
  '''
  view root page functions that returns the index page and its data
  '''

  news_sources = get_sources()
  print(news_sources)

  return render_template('index.html')
