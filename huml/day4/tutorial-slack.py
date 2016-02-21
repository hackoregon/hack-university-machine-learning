>>> import slacker
>>> u = slacker.Users()
>>> slacker.Users?
>>> u?
>>> u = slacker.Users(token=os.getenv('SLACK_TOKEN'))
>>> import os
>>> os.environ['SLACK_TOKEN']='xoxb-2069...88'
>>> slacker.Users(token=os.getenv('SLACK_TOKEN'))
>>> users.list
<bound method Users.list of <slacker.Users object at 0x7faa8de47bd0>>
>>> users.list()
<slacker.Response at 0x7faa8dbade90>
>>> resp = _
>>> resp.body
{u'cache_ts': 1456004324,
 u'members': [{u'color': u'3c8c69',
   u'deleted': False,
   u'id': u'U0MACP8QY',
   u'is_admin': False,
   u'is_bot': False,
   u'is_owner': False,
   u'is_primary_owner': False,
   u'is_restricted': False,
   u'is_ultra_restricted': False,
   u'name': u'1am5teph',
   u'profile': {u'avatar_hash': u'g8d70af86a21',
    u'email': u'marson.stephanie@gmail.com',
    u'image_192': u'https://secure.gravatar.com/avatar/8d70af86a21661b79910cd02f7e9fc38.jpg?s=192&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F7fa9%2Fimg%2Favatars%2Fava_0018-192.png',
...
 u'ok': True}
>>> users.list().body
{u'cache_ts': 1456006009,
 u'members': [{u'color': u'3c8c69',
   u'deleted': False,
   u'id': u'U0MACP8QY',
   u'is_admin': False,
   u'is_bot': False,
   u'is_owner': False,
   u'is_primary_owner': False,
   u'is_restricted': False,
   u'is_ultra_restricted': False,
   u'name': u'1am5teph',
   u'profile': {u'avatar_hash': u'g8d70af86a21',
    u'email': u'marson.stephanie@gmail.com',
...
 u'ok': True}
>>> users_dict = users.list().body
>>> d = users_dict['members'][0]
>>> d
{u'color': u'757575',
 u'deleted': False,
 u'id': u'USLACKBOT',
 u'is_admin': False,
 u'is_bot': False,
 u'is_owner': False,
 u'is_primary_owner': False,
 u'is_restricted': False,
 u'is_ultra_restricted': False,
 u'name': u'slackbot',
 u'profile': {u'avatar_hash': u'sv1444671949',
  u'email': None,
  u'fields': None,
  u'first_name': u'slackbot',
...
  u'last_name': u'',
  u'real_name': u'slackbot',
  u'real_name_normalized': u'slackbot'},
 u'real_name': u'slackbot',
 u'status': None,
 u'team_id': u'T0LKCU8EL',
 u'tz': None,
 u'tz_label': u'Pacific Standard Time',
 u'tz_offset': -28800}
>>> hist
>>> for d in users_dict['members']:
...     if d['name'] == 'hobs':
...         print json.dumps(d,indent=2)
...         break
>>> d
{u'color': u'e7392d',
 u'deleted': False,
 u'id': u'U0LL13TNV',
 u'is_admin': False,
 u'is_bot': False,
 u'is_owner': False,
 u'is_primary_owner': False,
 u'is_restricted': False,
 u'is_ultra_restricted': False,
 u'name': u'hobs',
 u'profile': {u'avatar_hash': u'g8eb2d80a351',
  u'email': u'hobsonlane@gmail.com',
  u'first_name': u'Hobson',
  u'image_192': u'https://secure.gravatar.com/avatar/8eb2d80a35122171463f423eeec7bfa4.jpg?s=192&d=https%3A%2F%2Fslack.global.ssl.fastly.net%2F7fa9%2Fimg%2Favatars%2Fava_0015-192.png',
...
  u'last_name': u'Lane',
  u'phone': u'5039746274',
  u'real_name': u'Hobson Lane',
  u'real_name_normalized': u'Hobson Lane',
  u'skype': u'codeninja1',
  u'title': u'Machine Intelligence'},
 u'real_name': u'Hobson Lane',
 u'status': None,
 u'team_id': u'T0LKCU8EL',
 u'tz': u'America/Los_Angeles',
 u'tz_label': u'Pacific Standard Time',
 u'tz_offset': -28800}
>>> for d in users_dict['members']:
...     print(d['title'])
...
>>> for d in users_dict['members']:
...     print(d.get('profile', {}).get('title', ''))
...
>>> history -o -p -f  tutorial-slack.py
