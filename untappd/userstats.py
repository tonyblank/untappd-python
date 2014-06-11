"""Untappd UserStats class."""

class UserStats(object):
  """Class to hold data from the user->stats."""

  def __init__(self, json_data):
    self.total_badges = json_data.get('total_badges')
    self.total_friends = json_data.get('total_friends')
    self.total_checkins = json_data.get('total_checkins')
    self.total_beers = json_data.get('total_beers')
    self.total_created_beers = json_data.get('total_created_beers')
