#!/usr/bin/python

from grammar      import Grammar

from mode         import Mode, named_modes
from buttons      import Buttons, AnyButtons
from button_press import ButtonPress
from binding      import Binding


def parse_mode(mode_block_p):
	if "alias" in mode_block_p:
		return named_modes[mode_block_p["alias"]]
	elif "literal" in mode_block_p:
		return Mode(*mode_block_p["literal"])
	else:
		raise Exception("Error parsing mode.")


def parse_button_press(binding_p, mode):
	hold = "hold" in binding_p
	middle_switch = "middle_switch" in binding_p
	
	buttons = None
	
	if "chord" in binding_p:
		buttons = Buttons(list(binding_p["chord"]), hold, middle_switch)
	elif "literal" in binding_p:
		buttons = Buttons([binding_p["literal"]], hold, middle_switch)
	elif "grouping" in binding_p:
		group_type = binding_p["grouping"]["type"]
		group = dict((e["button"], e["name"]) for e in binding_p["grouping"]["elements"][0])
		if group_type == "any":
			buttons = AnyButtons(group, hold, middle_switch)
	else:
		buttons = Buttons([], hold, middle_switch,)
	
	return ButtonPress(mode, buttons)


def parse(string):
	parsed = Grammar.parseString(string, parseAll = True)
	
	bindings = []
	
	for mode_block_p in parsed:
		mode = parse_mode(mode_block_p)
		
		for binding_p in mode_block_p["bindings"][0]:
			press = parse_button_press(binding_p, mode)
			
			call = binding_p["action"]["url"]
			args = list(binding_p["action"]["args"])
			bindings.append(Binding(press, call, args, "property" in binding_p))
	
	return bindings

