#!/usr/bin/python

from parser import parse
from client import Client

if __name__ == "__main__":
	bindings = parse(open("music.pom", "r").read())
	Client(bindings).run()
