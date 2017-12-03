# Check if users are following you back
Some users on Github try to trick you by following you and once you've followed them back, they unfollow you. This script gets rid of that problem by using the Github api to detect which of the people you follow is not following you back.

## Requirements
* Python 3.6
* The ``urllib`` module

## Usage
Use one of these:
* ``./notfollowback.py {yourusername}``
* ``python3 notfollowback.py {yourusername}``
* ``python notfollowback.py {yourusername}``

## Notes
* Python is awesome
* For the time being it only supports 100 followers. Once I have more time, I'll update it to work with more than 100 followers.
* PEP8 compliant