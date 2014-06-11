"""Untappd BreweryContact class."""

class BreweryContact(object):
  """Class to hold data from the brewery->contact."""

  def __init__(self, json_data):
    self.url = json_data.get('url')
    self.twitter = json_data.get('twitter')
    self.facebook = json_data.get('facebook')
    self.instagram = json_data.get('instagram')
