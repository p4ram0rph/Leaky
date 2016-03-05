import sys
import argparse

from api.he import *
from api.psbdmp import *
from api.viewdns import *

he		= HEsearch()
psb		= PSBsearch()
viewdns = dns()

parser 	= argparse.ArgumentParser( sys.argv[0].split('/')[0] , add_help=True)

parser.add_argument( "-f", help="Import emails/domain from file", required=False )
parser.add_argument( "-d", help="Domain(s) to search", required=False)
parser.add_argument( "-e", help="Email(s) to search", required=False)
args = vars( parser.parse_args() )

if args["f"]:
	with open(args["f"]) as line:
		shit = []
		for i in line: shit.append(i)
	if args["d"]:

		for domains in shit:
			try:
				viewdns.search(domains)
				psb.search(domains)
				psb.getResults() 
			except Exception, e:
				print e
	elif args["e"]:
		for emails in shit:
			try:
				psb.search(emails)
				psb.getResults()
				he.search(emails)
				he.getResults()
			except Exception, e:
				print e

elif args["e"]:
	email = args["e"]
	try:
		psb.search(email)
		psb.getResults()
		he.search(email)
		he.getResults()
	except Exception, e:
		print e

elif args["d"]:
	domain = args["d"]
	try:
		viewdns.search(domain)
		psb.search(domain)
		psb.getResults()
	except Exception, e:
		print e

else:
	print "python %s -h for usage" % sys.argv[0]