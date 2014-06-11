"""Untappd BreweryLocation class."""

class BreweryLocation(object):
  """Class to hold data from the brewery->location."""

  def __init__(self, json_data):
    self.brewery_city = json_data.get('brewery_city')
    self.brewery_state = json_data.get('brewery_state')
    self.lng = json_data.get('lng')
    self.lat = json_data.get('lat')
  