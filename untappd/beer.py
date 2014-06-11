"""Untappd Beer class."""

class Beer(object):
  """Class to hold data from the user->stats."""

  def __init__(self, json_data):
    self.auth_rating = json_data.get('auth_rating')
    self.beer_description = json_data.get('beer_description')
    self.bid = json_data.get('bid')
    self.beer_style = json_data.get('beer_style')
    self.beer_name = json_data.get('beer_name')
    self.wish_list = json_data.get('wish_list')
    self.beer_abv = json_data.get('beer_abv')
    self.beer_label = json_data.get('beer_label')
