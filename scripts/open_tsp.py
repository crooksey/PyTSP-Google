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
url_basic = "http://open.mapquestapi.com/directions/v2/route?key=" + my_app_key
# Important, we need to add headers saying we are posting JSON
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

# build the request
r = requests.post(url, data=json.dumps(route), headers=headers)
r_basic = requests.post(url_basic, data=json.dumps(route), headers=headers)
# load the json respone into the praser 
route_json = json.dumps(r.json(), indent=2)
route_json_basic = json.dumps(r_basic.json(), indent=2)
# load into a python data structure
data = json.loads(route_json)
data_basic = json.loads(route_json_basic)

# Map URL to generate a map showing the routes we are taking on this trip
map_placeholder = "http://open.mapquestapi.com/staticmap/v4/getmap?key={my_app_key}&bestfit={bestfit}&shape={shape}&size=600,600&type=map&imagetype=jpeg"

# Define some functions to return clean data
def get_bounding_box(data):
	# load the bounding box data which forms the edges
	# of the static map we will be using
	bestfit = "{lat1},{long1},{lat2},{long2}"
	bestfit_clean = bestfit.format(lat1=data['ul']['lat'], 
		long1=data['ul']['lng'], lat2=data['lr']['lat'], 
		long2=data['lr']['lng'])
	# now return the clean variable for use in the static map url
	return bestfit_clean

def get_shape(data):
	seq = ""
	for x in data['locations']:
		latLng = str(x['displayLatLng']['lat']) + ',' + str(x['displayLatLng']['lng']) + ','
		seq = seq + latLng
	# remove last trailing comma
	shape_clean = seq[:-1]
	return shape_clean

# run data through the functions
shape_basic = get_shape(data_basic['route'])
shape_optimised = get_shape(data['route'])
bestfit_basic = get_bounding_box(data_basic['route']['boundingBox'])
bestfit_optimised = get_bounding_box(data['route']['boundingBox'])

# generate map URL
map_basic = map_placeholder.format(my_app_key=my_app_key, bestfit=bestfit_basic, 
	shape=shape_basic)
map_optimised = map_placeholder.format(my_app_key=my_app_key, bestfit=bestfit_optimised,
	shape=shape_optimised)

# Get a printout of the data
print '>------------<'
print 'Original Route'
print '>------------<'
# Show original order
for x in data_basic['route']['locationSequence']:
	print route['locations'][int(x)]['latLng']['lat']
print "Total Distance " + str(data_basic['route']['distance']) + ' miles'
print "Total Fuel Used " + str(data_basic['route']['fuelUsed']) + ' litres'
print "Total Time " +  str(data_basic['route']['formattedTime'])
print 'Map ' + map_basic
print ''
print '>-------------<'
print 'Optimised Route'
print '>-------------<'
# Show optimised order
for x in data['route']['locationSequence']:
	print route['locations'][int(x)]
print "Total Distance " + str(data['route']['distance']) + ' miles'
print "Total Fuel Used " + str(data['route']['fuelUsed']) + ' litres'
print "Total Time " +  str(data['route']['formattedTime'])
print 'Map ' + map_optimised


