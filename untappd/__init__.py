"""Module docstring."""
import logging
import requests
import urllib

from checkin import Checkin
from user import User


class Untappd(object):
  """Class that handles auth and makes requests.

  Parameters:
    api_key - string
    api_secret - string
  """

  def __init__(self, client_id, client_secret, access_token=None, url_base='https://api.untappd.com/v4', debug=None):
    """Docstring."""
    self.client_id = client_secret
    self.client_secret = client_secret
    self.url_base = url_base
    self.access_token = access_token

    # set these to none to be populated later
    self.rate_limit_limit = None
    self.rate_limit_remaining = None

  def _check_response(self, response):
    """Docstring."""
    # get json
    response_json = response.json()

    # check status code
    if response_json['meta']['code'] == 200:
      # Time for a cold one!
      return response_json
    else:
      raise Exception

    # update rate limit info from headers


  def _request(self, endpoint, method, params):
    """Docstring."""
    url = '/'.join([self.url_base, endpoint])

    if method == 'GET':
      response = requests.get(url, params=params)

    # check response to make sure it worked!
    return self._check_response(response)

  def get_redirect_url(self, redirect_url):
    """Docstring."""
    url_base = 'https://untappd.com/oauth/authenticate/'

    params = {'client_id': self.client_id, 'response_type': 'code', 'redirect_url': redirect_url}

    url = '?'.join([url_base, urllib.urlencode(params)])

    return url

  def get_user_info(self, username, compact=None):
    """Docstring."""
    endpoint = 'user/info/%s' % username
    method = 'GET'

    params = {}

    if self.access_token:
      params['access_token'] = self.access_token

    if compact:
      params['compact'] = 'true'

    # pass params, method, endpoint to request method and get data!
    response = self._request(endpoint, method, params)

    user = User(response['response']['user'])

    return user

  def get_user_feed(self, username, max_id=None, limit=None):
    """Docstring."""
    endpoint = 'user/checkins/%s' % username
    method = 'GET'

    params = {}

    if self.access_token:
      params['access_token'] = self.access_token

    if max_id:
      params['max_id'] = max_id

    if limit:
      params['limit'] = limit

    response = self._request(endpoint, method, params)

    pagination = response['response']['pagination']
    max_id = pagination.get('max_id')

    checkins_data = response['response']['checkins']
    checkins_count = checkins_data.get('count')

    if checkins_count:
      checkins = []
      for checkin in response['response']['checkins']['items']:
        checkins.append(Checkin(checkin))
    else:
      checkins = None

    data = {
      'max_id': max_id,
      'checkins': checkins
    }

    return data

  def get_checkins_after_date(self, username, target_datetime, limit=25):
    """Gets all checkins since a given datetime object."""
    # holds our checkins
    checkins_results = []
    current_checkins = []
    max_id = None
    break_loop = False

    while True:
      checkin_data = self.get_user_feed(username, max_id=max_id, limit=limit)
      current_checkins = checkin_data['checkins']
    
      # check for edge case that query did not return any results
      if not current_checkins:
        break

      max_id = checkin_data['max_id']
        
      # iterate and append checkins to checkins_results if created_at >= target_datetime
      for checkin in current_checkins:
        if checkin.created_at >= target_datetime:
          checkins_results.append(checkin)
        else:
          # we've found the last checkin!
          print 'found last checkin!'
          break_loop = True
          break

      if break_loop:
        break

      # text break condition if there's no more checkins
      if len(current_checkins) != limit:
        break
    
    return checkins_results