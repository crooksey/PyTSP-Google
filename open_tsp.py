import requests
import json

# set your app key
my_app_key = "YOUR_KEY"

# add points to the route
route = {"locations":[]}
route['locations'].append( {"latLng":{"lat":51.524410144966154,"lng":-0.12989273652335526}})
route['locations'].append( {"latLng":{"lat":51.54495915136182,"lng":-0.16518885449221493}})
route['locations'].append( {"latLng":{"lat":51.52061842826141,"lng":-0.1495479641837033}})
route['locations'].append( {"latLng":{"lat":51.52850609658769,"lng":-0.20170525707760403}})

# url to post of API
url = "http://open.mapquestapi.com/directions/v2/optimizedroute?key=" + my_app_key
# Important, we need to add headers saying we are posting JSON
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

# build the request
r = requests.post(url, data=json.dumps(route), headers=headers)
# load the json respone into the praser 
route_json = json.dumps(r.json(), indent=2)
# load into a python data structure
data = json.loads(route_json)

print "Total Distance " + str(d2['route']['distance']) + ' miles'
print "Total Fuel Used " + str(d2['route']['fuelUsed']) + ' litres'
print "Total Time " +  str(d2['route']['formattedTime'])





