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
from os.path import exists, dirname, join, expanduser
from os import mkdir

rootpath = dirname(sys.argv[0])
ttpath = expanduser("~/.config/timetracker")
if not exists(ttpath):
	mkdir(ttpath)
dbpath = join(ttpath, "actions")
user = join(ttpath, "user")

from gi.repository import Gtk, GObject
from gi.repository import PanelApplet
import json
from urllib import urlopen
from actions_pb2 import All, LeftoverAction, StoredAction
from time import mktime, localtime

from settings import *

builder = Gtk.Builder()
builder.add_from_file(join(rootpath,"applet.builder"))

def getData(name):
	data = urlopen(timetracker+name).read()
	data = json.loads(data)
	return sorted([x["name"] for x in data if x["active"]])

def pickUser():
	users = getData("users")
	return u"TomP" # FIXME

def setText(applet):
	global button
	print "action", applet.act
	if applet.act.project == "IDLE":
		button.set_label("<IDLE>")
	elif applet.act.bug != "":
		if applet.act.description != "":
			button.set_label("%s: #%s: %s"%(applet.act.project, applet.act.bug, applet.act.description))
		else:
			button.set_label("%s: #%s"%(applet.act.project, applet.act.bug))
	elif applet.act.description != "":
		button.set_label("%s: %s"%(applet.act.project, applet.act.description))
	else:
		button.set_label("%s: %s"%(applet.act.project, applet.act.activity))

def buildCombo(ident, items, current):
	cmb = builder.get_object(ident)
	cmb.set_property("entry-text-column", 0) # workaround for #612396 (see comment #50)
	store = Gtk.ListStore(GObject.TYPE_STRING)
	cmb.set_model(store)
	cell = Gtk.CellRendererText()
	cmb.clear()
	cmb.pack_start(cell, True)
	cmb.add_attribute(cell, 'text', 0)
	index = 0
	for i, p in enumerate(items):
		cmb.append_text(p)
		if p == current:
			index = i
	cmb.set_active(index)
	return cmb

def getCombo(cmb):
	return cmb.get_active_text()

def idleAct():
	return getAct(
			{
				"project":"IDLE",
				"activity":"IDLE",
				"bug": "",
				"description": ""
			})

def getText(ident):
	ent = builder.get_object(ident)
	return ent.get_text()

def getAct(newAct):
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

def newAction(applet):
	projects = getData("projects")
	activities = getData("activities")

	cmbProject = buildCombo("cmbProject", projects, applet.act.project)
	cmbActivity = buildCombo("cmbActivity", activities, applet.act.activity)
	dialog = builder.get_object("dlgChooseAction")

	dialog.show_all()
	res = dialog.run()
	dialog.hide()

	if res == 1:
		newAct = {"project":getCombo(cmbProject), "activity": getCombo(cmbActivity), "bug":getText("entBug"), "description": getText("entDescription")}
		return getAct(newAct)
	elif res == 3:
		return idleAct()
	else:
		return applet.act

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
			if store.project == applet.act.project and store.activity == applet.act.activity and \
				store.bug == applet.act.bug and \
				(store.description == applet.act.description or store.bug != ""):
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
	open(dbpath,"wb").write(db.SerializeToString())

def setNewAction(button, applet):
	applet.act = newAction(applet)
	setText(applet)

def applet_factory(applet, iid, data = None):
	global db, button

	db = All()
	try:
		db.ParseFromString(open(dbpath).read())
	except IOError, e:
		print e
		pass
	button = Gtk.Button("It works!")
	button.connect("clicked", setNewAction, applet)
	applet.add(button)
	applet.show_all()
	#pickUser()
	applet.act = idleAct()
	setText(applet)
	saveDb()

	GObject.timeout_add(1000, another_second, applet)
	return True
				
if __name__ == '__main__':	# testing for execution
	print('Starting factory')

	if len(sys.argv) > 1 and sys.argv[1] == '-d': # debugging
		mainWindow = Gtk.Window()
		mainWindow.set_title('Applet window')
		mainWindow.connect('destroy', Gtk.main_quit)
		applet_factory(mainWindow, None)
		mainWindow.show_all()
		Gtk.main()
		sys.exit()
	else:
		PanelApplet.Applet.factory_main("TimetrackerWidgetFactory", PanelApplet.Applet.__gtype__, applet_factory, None)
