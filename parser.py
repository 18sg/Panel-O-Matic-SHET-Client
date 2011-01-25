#!/usr/bin/python

from grammar import grammar

parsed = grammar.parseString("""
	MUSIC {
		0 => /test "wacky" "woot";
		0123 => /test "wacky" "woot";
		_any( 0:"james"
		    , 1:"jonny"
		    , 2:"karl"
		    , 3:"matt"
		    , 4:"tom") => /shelf/copy_playlists;
	}
	0:1 {
		0 => /test "wacky" "woot";
	}
""", parseAll = True)


for mode_block in parsed:
	mode = mode_block["mode"]
	bindings = mode_block["bindings"][0]
	print "Mode:", mode
	
	for binding in bindings:
		hold = "hold" in binding
		middle_switch = "middle_switch" in binding
		print "\tBinding: Hold:", hold, "MS:", middle_switch
		
		print "\t\tCall:", binding["action"]["url"]
		for arg in binding["action"]["args"]:
			print "\t\t\t", arg
		
		if "chord" in binding:
			print "\t\tChord", list(binding["chord"])
		elif "literal" in binding:
			print "\t\tLiteral", binding["literal"]
		elif "grouping" in binding:
			group_type = binding["grouping"]["type"]
			group = dict((e["button"], e["name"]) for e in binding["grouping"]["elements"][0])
			print "\t\tGrouping", group_type, group
