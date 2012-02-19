#!/usr/bin/env python
from gi.repository import Gtk, GObject
from gi.repository import PanelApplet

def applet_fill(applet):
	label = Gtk.Label("Hello World")
	applet.add(label)
	applet.show_all()

def applet_factory(applet, iid, data):
	applet_fill(applet)
	return True

if __name__ == "__main__":
	PanelApplet.Applet.factory_main("TimetrackerWidgetFactory",
									PanelApplet.Applet.__gtype__,
									applet_factory, None)
