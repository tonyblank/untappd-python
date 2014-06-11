"""Untappd RecentBrews class."""

from beer import Beer
from brewery import Brewery

class RecentBrews(object):
  """Class to hold data for RecentBrews."""

  def __init__(self, json_data):
    self.beer = Beer(json_data.get('beer')) if json_data.get('beer') else None
    self.brewery = Brewery(json_data.get('brewery')) if json_data.get('brewery') else None
