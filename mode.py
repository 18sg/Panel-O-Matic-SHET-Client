#!/usr/bin/python


class Mode(object):
	
	def __init__(self, mode_type, mode):
		self.mode_type = mode_type
		self.mode      = mode
	
	
	def __eq__(self, other):
		return (self.mode_type == other.mode_type and 
		        self.mode == other.mode)
	
	
	def __hash__(self):
		return hash(self.mode_type) ^ hash(self.mode)
	
	
	def __repr__(self):
		return "Mode(%d, %d)"%(self.mode_type, self.mode)


named_modes = {
	"MUSIC"   : Mode(1, 0),
	"BROWSER" : Mode(1, 1),
	"WASHING" : Mode(1, 2),
	
	"JAMES"   : Mode(2, 0),
	"JONATHAN": Mode(2, 1),
	"KARL"    : Mode(2, 2),
	"MATT"    : Mode(2, 3),
	"TOM"     : Mode(2, 4),
}
