"""Untappd Media class. (partial support, only photos - other stuff seems redundant?)"""

from beer import Beer
from brewery import Brewery
from mediaphoto import MediaPhoto

class Media(object):
  """Class to hold data for Media."""

  def __init__(self, json_data):
    self.photo_id = json_data.get('photo_id')
    self.photo = MediaPhoto(json_data.get('photo')) if json_data.get('photo') else None
    self.created_at = json_data.get('created_at')
    self.venue = None # UNSUPPORTED NOW json_data.get('venue')
    self.checkin_id = json_data.get('checkin_id')
    self.beer = Beer(json_data.get('beer')) if json_data.get('beer') else None
    self.user = None # UNSUPPORTED NOW json_data.get('user')
    self.brewery = Brewery(json_data.get('brewery')) if json_data.get('brewery') else None
