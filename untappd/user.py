"""Untappd User class."""

from beer import Beer
from brewery import Brewery
from usercontact import UserContact
from media import Media
from recentbrews import RecentBrews
from userstats import UserStats

class User(object):
  """Class to hold data from the user."""

  def __init__(self, json_data):
    self.id = json_data.get('id')
    self.user_name = json_data.get('user_name')
    self.first_name = json_data.get('first_name')
    self.last_name = json_data.get('last_name')
    self.user_avatar = json_data.get('user_avatar')
    self.is_private = json_data.get('is_private')
    self.location = json_data.get('location')
    self.url = json_data.get('url')
    self.bio = json_data.get('bio')
    self.relationship = json_data.get('relationship')
    self.untappd_url = json_data.get('untappd_url')
    self.account_type = json_data.get('account_type')
    self.stats = UserStats(json_data.get('stats')) if json_data.get('stats') else None
    self.media =  self._media_list(json_data.get('media'))
    self.recent_brews = self._recent_brews_list(json_data.get('recent_brews'))
    self.contact = UserContact(json_data.get('contact')) if json_data.get('contact') else None
    self.date_joined = json_data.get('date_joined') # convert to datetime
    self.settings = None # NOT SUPPORTED UserSettings(json_data.get('settings'))
    self.is_supporter = json_data.get('is_supporter')
    self.user_cover_photo = json_data.get('user_cover_photo')
    self.user_cover_photo_offset = json_data.get('user_cover_photo_offset')
    self.last_name = json_data.get('last_name')
    self.user_avatar_hd = json_data.get('user_avatar_hd')
    self.checkins = None # NOT SUPPORTED

  def _media_list(self, json_data):
    """Docstring."""
    if json_data and json_data['count']:
      return [Media(i) for i in json_data.get('items')]
    else:
      return None

  def _recent_brews_list(self, json_data):
    """Docstring."""
    if json_data and json_data['count']:
      return [RecentBrews(i) for i in json_data.get('items')]
    else:
      return None
