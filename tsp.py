

################################################################### Start and finish at same place ######## go via, with route optimise ##
url= "https://maps.googleapis.com/maps/api/directions/json?origin=Portsmouth,UK&destination=Portsmouth,UK&waypoints=optimize:true|Southampton,UK|Poole,UK|Reading,UK|Bridport,Dorset&sensor=false&key=YOURAPIKEYHERE"
import urllib2
data = urllib2.urlopen(url)


pre_json = data.read()
import json
obj = json.loads(pre_json)
data_new = json.dumps(obj, indent=2)
#load into dict
d = json.loads(data_new)

routes = []

start_address = d['routes'][0]['legs'][0]['start_address']
start_lat = d['routes'][0]['legs'][0]['start_location'][u'lat']
start_long = d['routes'][0]['legs'][0]['start_location'][u'lng']

routes.append({'address': start_address, 'lat': start_lat, 'lng': start_long})
total_time = 0
total_distance = 0
for x in d['routes'][0]['legs']:
	total_time += x['duration']['value']
	total_distance += x['distance']['value']
	address = x['end_address']
	lat = x['end_location'][u'lat']
	lng = x['end_location'][u'lng']
	routes.append({'address': address, 'lat': lat, 'lng': lng})
print '##############################################################################'
print 'Optimised Route'
print '##############################################################################'
tt = (total_time / 3600.00)
td = total_distance*0.000621371192
print "Total Time %.2f hours" % round(tt,2)
print "Total Distance %.2f miles" % round(td,2)
for x in routes:
	print x

## ORIG ROUTE ##

url2 = "https://maps.googleapis.com/maps/api/directions/json?origin=Portsmouth,UK&destination=Portsmouth,UK&waypoints=|Southampton,UK|Poole,UK|Reading,UK|Bridport,Dorset&sensor=false&key=YOURAPIKEYHERE"
data2 = urllib2.urlopen(url2)

pre_json2 = data2.read()
import json
obj2 = json.loads(pre_json2)
data_new2 = json.dumps(obj2, indent=2)
#load into dict
d2 = json.loads(data_new2)

routes2 = []

start_address2 = d2['routes'][0]['legs'][0]['start_address']
start_lat2 = d2['routes'][0]['legs'][0]['start_location'][u'lat']
start_long2 = d2['routes'][0]['legs'][0]['start_location'][u'lng']

routes2.append({'address': start_address, 'lat': start_lat, 'lng': start_long})
total_time2 = 0
total_distance2 = 0

for x in d2['routes'][0]['legs']:
	total_time2 += x['duration']['value']
	total_distance2 += x['distance']['value']
	address = x['end_address']
	lat = x['end_location'][u'lat']
	lng = x['end_location'][u'lng']
	routes2.append({'address': address, 'lat': lat, 'lng': lng})
print '##############################################################################'
print 'Original Route'
print '##############################################################################'
tt2 = (total_time2 / 3600.00)
td2 = total_distance2*0.000621371192
print "Total Time %.2f hours" % round(tt2,2)
print "Total Distance %.2f miles" % round(td2,2)
for x in routes2:
	print x

print '##############################################################################'
print 'Summary'
print '##############################################################################'
total_saving_time = tt2 - tt
total_saving_distance = td2 - td
print 'The optimised route is %.2f miles shorter' % round(total_saving_distance,2)
print 'And also saves %.2f hours of time' % round(total_saving_time,2)
