from newsapi import NewsApiClient
from .models.source import Source

#get api key
api_key = None

def configure_request(app):
  '''
  initial configuration for important variables
  '''

  global api_key
  api_key = app.config['NEWS_API_KEY']

def get_sources():
  '''
  function that gets sources from api
  '''

  api = NewsApiClient(api_key=api_key)
  news_sources_data = api.get_sources()
  news_sources = []

  for source in news_sources_data['sources']:
    news_sources.append(
      Source(
        source.get('id'),
        source.get('name'),
        source.get('description'),
        source.get('url'),
        source.get('category'),
        source.get('language'),
        source.get('country')
      )
    )

  return news_sources
