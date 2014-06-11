"""Untappd UserContact class."""

class UserContact(object):
  """Class to hold data from the user->contact."""

  def __init__(self, json_data):
    self.twitter = json_data.get('twitter')
    self.foursquare = json_data.get('foursquare')
    self.facebook = json_data.get('facebook')
