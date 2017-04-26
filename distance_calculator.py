#Answering the question: Which NBA teams have the most distance between them?
#The WolframAlpha API returns the miles between two locations.

import urllib2
from xml.etree import cElementTree as ET
appID = "GUJ6PG-PK9RG8VL6K" #specific to this program


def miles_between(city1, city2):
	query = "Distance+between+" + city1 + "+and+" + city2
	url = "http://api.wolframalpha.com/v2/query?input="+query+"&appid="+str(appID)+"&includepodid=Result"
	s = urllib2.urlopen(url)
	contents = s.read()
	root = ET.fromstring(contents)

	distanceStr = root[0][0][1].text 
	#ignoring the " miles" at the end of the plaintext result
	return float(distanceStr[0:distanceStr.index(" ")])

#Note that you can pass in the same conference twice
def farthest_cities_within(conference1, conference2):
	maxDistance = ["city1", "city2", 0]
	while len(conference1) > 0:
		last = conference1.pop()
		for city in conference2:
			d = miles_between(last, city)
			print last + ", " + city + ": " + str(d)
			if d > maxDistance[2]:
				maxDistance[0] = last
				maxDistance[1] = city
				maxDistance[2] = d
	return maxDistance

atlantic = ["Boston", "New+York+City", "Philadelphia", "Toronto"]
central = ["Chicago", "Cleveland", "Auburn+Hills", "Indianapolis", "Milwaukee"]
southeast = ["Atlanta", "Charlotte", "Miami", "Orlando", "Washington+DC"]

northwest = ["Denver", "Minneapolis", "Oklahoma+City", "Portland", "Salt+Lake+City"]
pacific = ["Oakland", "LA", "Phoenix", "Sacramento"]
southwest = ["Dallas", "Houston", "Memphis", "New+Orleans", "San+Antonio"]

east = atlantic + central + southeast
west = northwest + pacific + southwest

print farthest_cities_within(east, west)
