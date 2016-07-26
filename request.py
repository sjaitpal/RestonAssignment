from urllib2 import Request, urlopen, URLError
import json

apikey = 'wghfdgpr78qwhwa4en4h6xu9'
testVar = raw_input()

request = Request('http://api.walmartlabs.com/v1/search?apiKey='+apikey+'&format=json&query='+testVar)

try:
	response = urlopen(request)
	JSON_dump = response.read()
	item_List = json.loads(JSON_dump)
	itemID = item_List['items'][0]['itemId']
except URLError, e:
	print 'No JSON data. Got an error code:', e
	
lookUp = Request('http://api.walmartlabs.com/v1/nbp?apiKey='+apikey+'&itemId='+str(itemID))
lookupItem = urlopen(lookUp)
JSON_dump_2 = lookupItem.read()
item_List_2 = json.loads(JSON_dump_2)
final_list = {}

for items in range(0,10):
	itemIDpro = item_List_2[items]['itemId']
	itemName = item_List_2[items]['name']
	lookupReview = Request('http://api.walmartlabs.com/v1/reviews/'+str(itemIDpro)+'?apiKey='+apikey+'&format=json')
	sum = 0
	
	try:
		review = urlopen(lookupReview)
		JSON_dump_3 = review.read()
		item_List_3 = json.loads(JSON_dump_3)
		if len(item_List_3['reviews']) != 0:
			for ratings in item_List_3['reviews']:
				sum += int(ratings['overallRating']['rating'])
			avgRating = sum / float(len(item_List_3['reviews']))
		else:
			avgRating=0
		final_list[itemName] = avgRating
		#print(itemName + ": Rating - " + str(avgRating))
		
	except URLError as e:
		print 'No JSON data ', e
		
print("UnSorted items --------------------------------------------")
for i in final_list:
	print(i + ' : ' + str(final_list[i]))
	
print("\n\nSorted items ----------------------------------------------")
for i, sort_Value in sorted(final_list.items(), key=lambda x: x[1], reverse=True):
	print(i + ' : ' + str(final_list[i]))