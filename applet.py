#!/usr/bin/python

"""

(C) Copyright 2011 Tom Parker

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

import sys

import gtk
import pygtk
import gnomeapplet
import json
from urllib import urlopen
from actions_pb2 import All, LeftoverAction, StoredAction
from time import mktime, localtime
import gobject

pygtk.require('2.0')

timetracker = "http://localhost:8000/"
timeModulo = 10

def getData(name):
	data = urlopen(timetracker+name).read()
	data = json.loads(data)
	return sorted([x["name"] for x in data if x["active"]])

def pickUser():
	users = getData("users")
	return u"TomP" # FIXME

def setText(applet):
	global label
	print "text", applet.act
	print "label", label
	if applet.act.bug == None:
		label.set_text("%s: %s"%(applet.act.project, applet.act.description))
	elif applet.act.description == None:
		label.set_text("%s: #%s"%(applet.act.project, applet.act.bug))
	else:
		label.set_text("%s: #%s: %s"%(applet.act.project, applet.act.bug, applet.act.description))

def newAction(parent):
	projects = getData("projects")
	activities = getData("activities")

	dialog = gtk.Dialog('Choose action')
	hbox = gtk.HBox(dialog)
	hbox.add(gtk.Label("foo"))
	dialog.show_all()
	#res = dialog.run()
	#print "res", res
	dialog.hide()

	# FIXME
	newAct = {"project":projects[0], "activity":activities[0], "bug":"1234", "description": "description"}
	
	for act in db.leftovers:
		if act.project == newAct["project"] \
			and act.activity == newAct["activity"] \
			and act.bug == newAct["bug"] \
			and act.description == newAct["description"]:
				return act
	else:
		act = db.leftovers.add()
		act.project = newAct["project"]
		act.activity = newAct["activity"]
		act.bug = newAct["bug"]
		act.description = newAct["description"]
		act.secondsCount = 0
		return act

def another_second(applet):
	global db
	applet.act.secondsCount +=1
	saveDb()

	now = localtime()

	secondsToday = (60*((60*now.tm_hour) + now.tm_min)) + now.tm_sec
	timeMod = secondsToday % timeModulo
	print secondsToday, timeMod

	if timeMod == 0:
		start = int(mktime(now)-timeModulo)
		end = int(mktime(now))
		match = ("project", "activity", "bug", "description")
		for store in db.stored:
			for field in match:
				if getattr(store, field) != getattr(applet.act, field):
					break
			else:
				if store.end == start:
					store.end = end
					break
		else:
			store = db.stored.add()
			for field in match:
				setattr(store, field, getattr(applet.act, field))
			store.start = start
			store.end = end
		applet.act.secondsCount -= timeModulo
		saveDb()
		print "hit modulo"
		print applet.act
		print store

	return True

def saveDb():
	open("actions","wb").write(db.SerializeToString())

def applet_factory(applet, iid):
	global db, label

	db = All()
	try:
		db.ParseFromString(open("actions").read())
	except IOError, e:
		print e
		pass
	label = gtk.Label("It works!")
	applet.add(label)
	applet.show_all()
	pickUser()
	applet.act = newAction(applet)
	setText(applet)
	saveDb()

	gobject.timeout_add(1000, another_second, applet)
	return True
            
if __name__ == '__main__':   # testing for execution
   print('Starting factory')

   if len(sys.argv) > 1 and sys.argv[1] == '-d': # debugging
      mainWindow = gtk.Window()
      mainWindow.set_title('Applet window')
      mainWindow.connect('destroy', gtk.main_quit)
      applet = gnomeapplet.Applet()
      applet_factory(applet, None)
      applet.reparent(mainWindow)
      mainWindow.show_all()
      gtk.main()
      sys.exit()
   else:
      gnomeapplet.bonobo_factory('OAFIID:SampleApplet_Factory', 
                                 gnomeapplet.Applet.__gtype__, 
                                 'Sample applet', '0.1', 
                                 applet_factory)
