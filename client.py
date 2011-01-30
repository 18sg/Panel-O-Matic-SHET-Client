#!/usr/bin/python

import os, os.path, sys

from twisted.internet import reactor
from twisted.internet import inotify
from twisted.python   import filepath

from shet.client import ShetClient

from parser       import parse
from mode         import Mode
from buttons      import Buttons
from button_press import ButtonPress


class Client(ShetClient):
	
	def __init__(self, bindings_dir, *args, **kwargs):
		
		ShetClient.__init__(self, *args, **kwargs)
		
		self.bindings_dir = bindings_dir
		self.bindings = []
		self.load_bindings()
		
		# Setup inotify
		self.notifier = inotify.INotify()
		self.notifier.startReading()
		self.notifier.watch(filepath.FilePath(self.bindings_dir),
		                    callbacks = [self.notify])
		
		self.watch_event("/lounge/panel/pressed", self.on_btn_pressed)
		
		print "Button monitor started..."
	
	
	def notify(self, notifier, filepath, mask):
		if filepath.path.endswith(".pom"):
			print "\033[2J" # Clear the screen
			self.load_bindings()
	
	
	def load_bindings(self):
		bindings = []
		for file in filter((lambda n: n.endswith(".pom")),
		                   os.listdir(self.bindings_dir)):
			file = os.path.join(self.bindings_dir, file)
			try:
				print "Reading %s"%file,
				bindings += parse(open(file, "r").read())
				print "OK."
			except Exception, e:
				print "Error parsing bindings:", e
		
		self.bindings = bindings
		print "Done loading bindings."
	
	
	def on_btn_pressed(self, data):
		mode_data, button_data = data
		mode    = Mode(*mode_data)
		buttons = Buttons(*button_data)
		press   = ButtonPress(mode, buttons)
		
		for binding in self.bindings:
			if binding.is_triggered_by(press):
				args = binding.get_call(press)
				try:
					if binding.prop:
						self.set(*args)
					else:
						self.call(*args)
				except Exception, e:
					print e



if __name__ == "__main__":
	Client(sys.argv[1]).run()
