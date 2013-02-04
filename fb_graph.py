#!/usr/bin/python2.7
<<<<<<< HEAD
import fb
from simple_graph import *
from bcolors import bcolors

if __name__ == "__main__":

	#Collect Username and Password
	fb.auth()

	#Get Profile and Friends list
	profile = fb.queryJSON('me')
	friends = fb.queryJSON('me/friends')
	friends = friends['data']

	#Create graph of the data
=======
import facebook
import fb_auth
from bcolors import bcolors
from simple_graph import *

if __name__ == "__main__":
	ACCESS_TOKEN = fb_auth.authorize()
    
	graph = facebook.GraphAPI(ACCESS_TOKEN)
	profile = graph.get_object("me")
	friends = graph.get_connections("me", "friends")
	friends = friends['data']

>>>>>>> 7e6e41c9020060edc6699d38e1f5cbdc98229d34
	fg = Graph()
	fg.add_node(profile['id'], Node(profile))

	#add link from all to profile
	for f in friends:
		fg.add_node(f["id"], Node(f))
		fg.add_adjacent(profile['id'], fg.get_node(f["id"]))

<<<<<<< HEAD
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
			mutualfriends = fb.queryJSON(f['id']+"/mutualfriends")

			#check if they have the most mutual friends
=======
	average_mutual = 0
	max_mcount = 0
	max_mutual = None
	for f in friends:
		if f['id'] != profile['id']:
			print "Examining: ", f['name']
			mutualfriends = graph.get_connections(f['id'], "mutualfriends")
>>>>>>> 7e6e41c9020060edc6699d38e1f5cbdc98229d34
			mcount = len(mutualfriends['data'])
			if mcount > max_mcount:
				max_mutual = f['name']
				max_mcount = mcount

			average_mutual += mcount
<<<<<<< HEAD

			#a little output 
			print "--------->  %s%d mutual friends%s" % (bcolors.PURPLE, mcount, bcolors.ENDC)

			#add connections in graph between friends	
=======
			print "--------->  %s%d mutual friends%s" % (bcolors.PURPLE, mcount, bcolors.ENDC)		
>>>>>>> 7e6e41c9020060edc6699d38e1f5cbdc98229d34
			for m in mutualfriends['data']:
				if f['id'] != m['id']:
					fg.add_adjacent(f['id'], fg.get_node(m['id']))

<<<<<<< HEAD
	#output friend stats
=======
>>>>>>> 7e6e41c9020060edc6699d38e1f5cbdc98229d34
	average_mutual /= len(friends)-1
	print "\n\nAverage Number of Mutual Friends: 	%s" % average_mutual
	print "Max Number of Mutual Friends:		%s" % max_mutual

<<<<<<< HEAD
	################################################
	## Outputting to file --------------------------
	################################################

	#Create string buffer for large output
	strBuff = []
	strBuff.append('<gexf xmlns="http://www.gexf.net/1.2draft" version="1.2" xmlns:viz="http://www.gexf.net/1.2draft/viz"><graph mode="static" defaultedgetype="undirected"><nodes>\n')

	#output nodes
	for i, n in fg.nodes.iteritems():
		strBuff.append('<node id="' + n.data["id"] + '" label="'+ n.data["name"]+'" />\n')

	strBuff.append('</nodes>\n')
	strBuff.append('<edges>\n')

	#output edges
=======
	######################
	## Outputting to file
	######################

	stroutput = '<gexf xmlns="http://www.gexf.net/1.2draft" version="1.2" xmlns:viz="http://www.gexf.net/1.2draft/viz"><graph mode="static" defaultedgetype="undirected"><nodes>\n'

	#nodes
	for i, n in fg.nodes.iteritems():
		stroutput += '<node id="' + n.data["id"] + '" label="'+ n.data["name"]+'" />\n'

	stroutput += '</nodes>\n'
	stroutput += '<edges>\n'

	#edges
>>>>>>> 7e6e41c9020060edc6699d38e1f5cbdc98229d34
	count = 0
	for i, n in fg.nodes.iteritems():
		if n.data['id'] == profile['id']:
			color = {'r': "0", 'g': "0", 'b': "0"}
		else:
			color = {'r': "59", 'g': "89", 'b': "152"}
<<<<<<< HEAD

		for adjacent in n.adjacents:
			count += 1
			strBuff.append('<edge id="'+str(count)+'" source="'+n.data['id']+'" target="'+adjacent.data['id']+'">')
			strBuff.append('<viz:color r="'+color['r']+'" g="'+color['g']+'" b="'+color['b']+'"/>')
			strBuff.append('</edge>')

	strBuff.append('</edges></graph></gexf>\n')

	#handle any unicode characters in names.
	outputstr = ''.join(strBuff)
	outputstr = outputstr.decode("utf-8")

	f = open("output.gexf", 'w')
	f.write(outputstr)
=======
		for adjacent in n.adjacents:
			count += 1
			stroutput += '<edge id="'+str(count)+'" source="'+n.data['id']+'" target="'+adjacent.data['id']+'">'
			stroutput += '<viz:color r="'+color['r']+'" g="'+color['g']+'" b="'+color['b']+'"/>'
			stroutput +='</edge>'

	stroutput += '</edges></graph></gexf>\n'

	f = open("output.gexf", 'w')
	f.write(stroutput)
>>>>>>> 7e6e41c9020060edc6699d38e1f5cbdc98229d34
	f.close()
