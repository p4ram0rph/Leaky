import requests
import json

class PSBsearch( object ):

	def __init__( self ):
		self.api_url 		= "http://psbdmp.com/api/search/"


	def search( self, searchQuery ):
		if '@' in searchQuery:
			self.url 		= '%semail/%s' % (self.api_url, searchQuery)
		else:
			self.url 		= '%sdomain/%s' % (self.api_url, searchQuery)

		try:

			self.results 	= requests.get(str(self.url))
			print self.results

		except Exception, e:
			print e

	def getResults( self ):

		js = json.loads((self.results.text))

		if js["error"] == 0:

			print "Found %d entries for %s" % (js["count"], js["search"])			
			for i in js["data"]: print "Date: %s  Leak: http://pastebin.com/raw/%s " % (i["time"], i["id"])

		else:

			print "Not Found"



  