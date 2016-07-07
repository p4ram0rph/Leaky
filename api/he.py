import requests
import json

class HEsearch(  ):

	def __init__( self ):
		self.api_url = "https://hacked-emails.com/api?q="


	def search( self, searchQuery ):
		self.url = '%s%s' % (self.api_url, searchQuery)
		print self.url
		try:
			self.results = requests.get(str(self.url), verify=True)
			print self.results
		except Exception, e:
			pass

	def getResults( self ):
		js = json.loads((self.results.text))
		if js["status"] == "found":
			print "Found %d entries for %s" % (js["results"], js["query"])

			#print js["data"][0]


			for i in xrange(len(js["data"])):
				print "Title: %s Date: %s  Leak: %s Details: %s " %(
				 js["data"][i]["title"],
				 js["data"][i]["date_leaked"],
				 js["data"][i]["source_url"], 
				 js["data"][i]["details"]
				 )





