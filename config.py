import os

class Config:
  '''
  general configuration parent class
  '''

  MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
  SECRET_KEY = os.environ.get('SECRET_KEY')

  pass

class ProdConfig(Config):
  '''
  production configuration child class

  Args:
    Config: The Parent configuration class with general configuration settings
  '''

  pass

class DevConfig(Config):
  '''
  development configuration child class

  Args:
    Config: The Parent configuration class with general configuration settings
  '''

  DEBUG = True

config_options = {
  'development': DevConfig,
  'production': ProdConfig
}
