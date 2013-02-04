#!/usr/bin/python2.7
import fb_auth
from simple_graph import *
from bcolors import bcolors

if __name__ == "__main__":

	#Collect Username and Password
	fb_auth.auth()

	#Get Profile and Friends list
	profile = fb_auth.queryJSON('me')
	friends = fb_auth.queryJSON('me/friends')
	friends = friends['data']

	#Create graph of the data
	fg = Graph()
	fg.add_node(profile['id'], Node(profile))

	#add link from all to profile
	for f in friends:
		fg.add_node(f["id"], Node(f))
		fg.add_adjacent(profile['id'], fg.get_node(f["id"]))

	#variables for friend stats
	average_mutual = 0
	max_mcount = 0
	max_mutual = None

	#build graph for mutual friends
	for f in friends:
		#if not us
		if f['id'] != profile['id']:

			#get list of mutual friends
			print "Examining: ", f['name']
			mutualfriends = fb_auth.queryJSON(f['id']+"/mutualfriends")

			#check if they have the most mutual friends
			mcount = len(mutualfriends['data'])
			if mcount > max_mcount:
				max_mutual = f['name']
				max_mcount = mcount

			average_mutual += mcount

			#a little output 
			print "--------->  %s%d mutual friends%s" % (bcolors.PURPLE, mcount, bcolors.ENDC)

			#add connections in graph between friends	
			for m in mutualfriends['data']:
				if f['id'] != m['id']:
					fg.add_adjacent(f['id'], fg.get_node(m['id']))

	#output friend stats
	average_mutual /= len(friends)-1
	print "\n\nAverage Number of Mutual Friends: 	%s" % average_mutual
	print "Max Number of Mutual Friends:		%s" % max_mutual

	######################
	## Outputting to file
	######################

	stroutput = '<gexf xmlns="http://www.gexf.net/1.2draft" version="1.2" xmlns:viz="http://www.gexf.net/1.2draft/viz"><graph mode="static" defaultedgetype="undirected"><nodes>\n'

	#output nodes
	for i, n in fg.nodes.iteritems():
		stroutput += '<node id="' + n.data["id"] + '" label="'+ n.data["name"]+'" />\n'

	stroutput += '</nodes>\n'
	stroutput += '<edges>\n'

	#output edges
	count = 0
	for i, n in fg.nodes.iteritems():
		if n.data['id'] == profile['id']:
			color = {'r': "0", 'g': "0", 'b': "0"}
		else:
			color = {'r': "59", 'g': "89", 'b': "152"}
		for adjacent in n.adjacents:
			count += 1
			stroutput += '<edge id="'+str(count)+'" source="'+n.data['id']+'" target="'+adjacent.data['id']+'">'
			stroutput += '<viz:color r="'+color['r']+'" g="'+color['g']+'" b="'+color['b']+'"/>'
			stroutput +='</edge>'

	stroutput += '</edges></graph></gexf>\n'

	stroutput = stroutput.decode("utf-8")

	f = open("output.gexf", 'w')
	f.write(stroutput)
	f.close()
