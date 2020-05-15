import urllib
import jsonlib

# serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})

    print ('Retrieving ',url)
    url_handle = urllib.urlopen(url)
    data = url_handle.read()

    print ('Retrieved',len(data),'characters')
    json_data = jsonlib.loads(data)

    #print json.dumps(json_data['results'], indent=3)
    print ('Place id',json_data['results'][0]['place_id'])