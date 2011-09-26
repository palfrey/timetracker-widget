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
from actions_pb2 import All
from time import localtime

day = int(sys.argv[1])
month = int(sys.argv[2])

rootpath = dirname(sys.argv[0])
ttpath = expanduser("~/.config/timetracker")
if not exists(ttpath):
	mkdir(ttpath)
dbpath = join(ttpath, "actions")

db = All()
db.ParseFromString(open(dbpath).read())

for s in sorted(db.stored, key=lambda s:s.start):
	start = localtime(s.start)
	if start.tm_mday!=day or start.tm_mon!=month:
		continue
	end = localtime(s.end)
	print "%02d:%02d -"%(start.tm_hour,start.tm_min), 
	print "%02d:%02d"%(end.tm_hour,end.tm_min), 
	print s.project,"-",s.activity,"-", s.bug,"-", s.description

