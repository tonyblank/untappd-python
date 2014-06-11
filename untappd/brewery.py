"""Untappd Brewery class."""

from brewerycontact import BreweryContact
from brewerylocation import BreweryLocation

class Brewery(object):
  """Class to hold data from the Brewery."""

  def __init__(self, json_data):
    self.brewery_id = json_data.get('brewery_id')
    self.brewery_active = json_data.get('brewery_active')
    self.brewery_name = json_data.get('brewery_name')
    self.contact = BreweryContact(json_data.get('contact')) if json_data.get('contact') else None
    self.brewery_label = json_data.get('brewery_label')
    self.brewery_location = BreweryLocation(json_data.get('brewery_location')) if json_data.get('brewery_location') else None
    self.country_name = json_data.get('country_name')
