#!/usr/bin/python

class ButtonPress(object):
	
	def __init__(self, mode, buttons):
		self.mode    = mode
		self.buttons = buttons
	
	
	def __eq__(self, other):
		return (self.mode == other.mode and self.buttons == other.buttons)
	
	
	def __repr__(self):
		return "ButtonPress(%s, %s)"%(repr(self.mode), repr(self.buttons))
