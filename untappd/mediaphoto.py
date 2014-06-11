"""Untappd MediaPhoto class."""


class MediaPhoto(object):
  """Class to hold data for MediaPhoto."""

  def __init__(self, json_data):
    self.photo_img_md = json_data.get('photo_img_md')
    self.photo_img_lg = json_data.get('photo_img_lg')
    self.photo_img_sm = json_data.get('photo_img_sm')
    self.photo_img_og = json_data.get('photo_img_og')
