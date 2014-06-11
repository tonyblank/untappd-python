import untappd
from datetime import datetime, timedelta

u = untappd.Untappd(
  client_id='YOUR CLIENT ID',
  client_secret='YOUR CLIENT SECRET',
  access_token='A USERS ACCESS TOKEN'
)

thirty_days_ago = datetime.now() - timedelta(30)

checkins_after_date = u.get_checkins_after_date('hiredgun79', thirty_days_ago, limit=50)

most_recent_checkin = checkins_after_date[0]

# go drink a beer!
