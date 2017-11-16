#test.py
import sys
import requests

#Websites
#http://resources.infosecinstitute.com/ - Where you got the code from
#http://google.com/
req = requests.get('')
print('Response Code: ' + str(req.status_code))
print('\nResponse:\n' + req.text)
