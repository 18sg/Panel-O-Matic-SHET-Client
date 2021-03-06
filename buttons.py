#!/usr/bin/python


class Buttons(object):
	
	def __init__(self, chord = None, hold = False, middle_switch = False):
		self.chord         = chord or []
		self.hold          = hold
		self.middle_switch = middle_switch
	
	
	def get_inferred_arguments(self, actually_pressed):
		return []
	
	
	def __repr__(self):
		return "Buttons(%s, %s, %s)"%(repr(self.chord),
		                              repr(self.hold),
		                              repr(self.middle_switch))
	
	
	def __eq__(self, other):
		return (self.chord == other.chord
		        and self.hold == other.hold
		        and self.middle_switch == other.middle_switch)



class AnyButtons(Buttons):
	
	def __init__(self, any_of, *args):
		Buttons.__init__(self, None, *args)
		self.any_of = any_of
	
	
	def get_inferred_arguments(self, actually_pressed):
		args = [self.any_of[btn] for btn in filter((lambda btn: btn in self.any_of),
		                                           actually_pressed.buttons.chord)]
		return args
	
	
	def __eq__(self, other):
		try:
			match = self.any_of == other.any_of
		except AttributeError:
			match = set(other.chord).issubset(set(self.any_of.iterkeys()))
		
		return (match
		        and self.hold == other.hold
		        and self.middle_switch == other.middle_switch)
	
	
	def __repr__(self):
		return "AnyButtons(%s, %s, %s)"%(repr(self.any_of),
		                                 repr(self.hold),
		                                 repr(self.middle_switch))
