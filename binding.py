#!/usr/bin/python

class Binding(object):
	
	def __init__(self, button_press, call, args):
		self.button_press = button_press
		self.call         = call
		self.args         = args
	
	
	def get_call(self, actually_pressed):
		return ([self.call]
		        + self.button_press.buttons.get_inferred_arguments(actually_pressed)
		        + self.args)
	
	
	def is_triggered_by(self, button_press):
		return self.button_press == button_press
	
	
	def __repr__(self):
		return "Binding(%s, %s, %s)"%(repr(self.button_press),
		                              repr(self.call),
		                              repr(self.args))
