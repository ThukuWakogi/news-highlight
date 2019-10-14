from newsapi import NewsApiClient

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
  news_sources = api.get_sources()
  return news_sources
