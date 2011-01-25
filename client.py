#!/usr/bin/python

from shet.client import ShetClient

from mode         import Mode
from buttons      import Buttons
from button_press import ButtonPress


class Client(ShetClient):
	
	def __init__(self, bindings, *args, **kwargs):
		ShetClient.__init__(self, *args, **kwargs)
		
		self.bindings = bindings
		
		self.watch_event("/livingroom/btn_pressed", self.on_btn_pressed)
	
	
	def decode_mode(self, encoded):
		return Mode(encoded & 0b11, encoded >> 2)
	
	
	def decode_buttons(self, encoded, hold_e, middle_switch_e):
		return Buttons(filter((lambda n: bool((encoded>>n) & 0b1)),
		                      range(5)),
		               bool(hold_e),
		               bool(middle_switch_e))
	
	
	def on_btn_pressed(self, encoded):
		mode_e          = encoded >> 7
		buttons_e       = encoded & 0b11111
		hold_e          = (encoded >> 5) & 0b1
		middle_switch_e = (encoded >> 6) & 0b1
		
		mode    = self.decode_mode(mode_e)
		buttons = self.decode_buttons(buttons_e, hold_e, middle_switch_e)
		press   = ButtonPress(mode, buttons)
		
		for binding in self.bindings:
			if binding.is_triggered_by(press):
				args = binding.get_call(press)
				self.call(*args)

