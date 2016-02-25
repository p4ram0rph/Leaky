import requests
from BeautifulSoup import BeautifulSoup as Soup


class dns:
	def __init__( self ):
		self.api_url = "http://viewdns.info/iphistory/?domain="


	def search( self, searchQuery ):
		url  = '%s%s' % (self.api_url, searchQuery) 
		soup = Soup( requests.get(url).text )
		for table in soup.findAll( "table", { "border" : "1" } ):
			for tr in table.findAll( "tr" ):
				print tr.text
