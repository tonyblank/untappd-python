"""Untappd Checkins class."""

from datetime import datetime

from beer import Beer
from brewery import Brewery
from user import User

class Checkin(object):
  """Class to hold data from the Checkins."""

  def __init__(self, json_data):
    self.checkin_comment = json_data.get('checkin_comment')
    self.media = None # NOT SUPPORTED json_data.get('media')
    self.created_at = datetime.strptime(json_data.get('created_at'), '%a, %d %b %Y %H:%M:%S +0000') if json_data.get('created_at') else None
    self.venue = None # NOT SUPPORTED json_data.get('venue')
    self.checkin_id = json_data.get('checkin_id')
    self.comments = json_data.get('comments')
    self.source = None # NOT SUPPORTED json_data.get('source')
    self.beer = Beer(json_data.get('beer')) if json_data.get('beer') else None
    self.user = User(json_data.get('user')) if json_data.get('user') else None
    self.rating_score = json_data.get('rating_score')
    self.toasts = None # NOT SUPPORTED json_data.get('toasts')
    self.brewery = Brewery(json_data.get('brewery')) if json_data.get('brewery') else None
    self.badges = None # NOT SUPPORTED json_data.get('badges')
