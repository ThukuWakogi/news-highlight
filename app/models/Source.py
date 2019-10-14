class Source():
  '''
  defines source objects
  '''

  def __init__(self, id, name, description, url, category, language, country):
    '''
    requires for values upon object instanstiation
    '''

    self.id = id
    self.name = name
    self.description = description
    self.url = url
    self.category = category
    self.language = language
    self.country = country
