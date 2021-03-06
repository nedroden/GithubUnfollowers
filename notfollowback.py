#!/usr/bin/env python3

'''
Github Unfollower Check
-----------------------

Checks which users are not following you back. To use,
run this file from a terminal and provide the login name
of the user you want to check.

If desired, you can also import this module and call the
'run' function with the username as a parameter.

Version:    1.0.0
Author:     Robert Monden <dev [at] robertmonden [dot] com>
Copyright:  2017, Robert Monden

License:    MIT

'''

import sys
import json

from urllib import request
from urllib.error import *

__author__ = 'Robert Monden'
__copyright__ = 'Copyright 2017, Robert Monden'
__license__ = 'MIT'
__version__ = '1.0.0'
__email__ = 'dev@robertmonden.com'

headrs = {}


class HTTPRequest:
    response = None

    def __init__(self, url):
        try:
            rqst = request.Request(url, headers=headrs)
            self.response = request.urlopen(rqst)

        except (Exception, urllib.error.HTTPError) as e:
            throw_error('Cannot open url\n{0}'.format(e))

    def get_response(self):
        return self.response.read().decode()


def run(username):
    set_headers()

    url = 'https://api.github.com/users/{0}'.format(username) \
        + '/{0}?per_page=100'

    httprequest = HTTPRequest(url.format('followers'))
    str_followers = httprequest.get_response()

    httprequest = HTTPRequest(url.format('following'))
    str_following = httprequest.get_response()

    followers, following = parse_all(str_followers, str_following)

    for follower in following:
        if follower not in followers:
            print('{0} is not following you back'.format(follower))


def check_params():
    if len(sys.argv) is not 2:
        throw_error(
            'Invalid number of parameters.'
            'Usage: ./notfollowback.py {username}',
            True
        )


def throw_error(message, fatal=False):
    print('==> Error: {0}'.format(message))

    if fatal:
        sys.exit(1)


def set_headers():
    headrs['User-Agent'] = 'Mozilla/5.0'


def parse_all(usr_followers, usr_following):
    followers = [follower['login'] for follower in json.loads(usr_followers)]
    following = [following['login'] for following in json.loads(usr_following)]

    return (followers, following)


if __name__ == '__main__':
    check_params()
    run(sys.argv[1])
