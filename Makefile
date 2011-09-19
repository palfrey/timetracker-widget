all: actions_pb2.py

actions_pb2.py: actions.proto
	protoc --python_out=. actions.proto

load::
	python loader.py actions.txt actions

dump::
	python dumper.py actions actions.txt

.PHONY: load dump
