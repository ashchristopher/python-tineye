TinEye - Python app to screen-scrape TinEye image search results.
====================================

Install:
-------------
To install, put somewhere on your python path. Doesn't matter where.

Requirements:
---------------
I am using BeautifulSoup to parse the results output. If you want this
python program to work - best install BeautifulSoup. It very useful for
other things too.

About: 
--------------
You can use this app to search for photos on the TinEye webapp. 
Initially I had asked for non-commercial access to their API, but I got 
a PFO instead.

Using this library is in direct conflict with their terms of service. I 
have put in a few random User Agent strings and search rate limiting but 
come one. These guys design image search algorithms for a living. I am 
sure they can tell when their system is being abused. Make sure you 
steal your neighbors WiFi connection when using this code.

Usage:
---------
Usage is pretty simple. There are two objects, TinEye search object and 
a TinEye photo object. You create your images that you want searched and 
pass them to the TinEye search object.

	from tineye import TinEye, TinEyePhoto
	photo = TinEyePhoto(name='My Cool Photo', 
'http://example.com/wicked_photo.jpg')

	te = TinEye()
	num_results, link = te.search(photo)

See - it's not too tough.
