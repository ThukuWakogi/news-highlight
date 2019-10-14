from flask import render_template
from . import main
from ..requests import get_sources, get_articles_from_source

#views
@main.route('/')
def index():
  '''
  view root page functions that returns the index page and its data
  '''

  news_sources = get_sources()

  return render_template('index.html', news_sources=news_sources)

@main.route('/source/<source_name>')
def source(source_name):
  '''
  features story and returns source.html and its respective articles
  '''

  articles = get_articles_from_source(source_name)

  return render_template('source.html', articles=articles)
