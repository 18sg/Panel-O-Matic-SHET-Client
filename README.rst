Panel-O-Matic
=============

Panel-O-Matic: A SHET client which provides easy configuration of keybindings
for the button panel in our living room. Uses a custom configuration language
using pyparsing.

Fairly quick-and-hacked with a few hard-coded variables where there shouldn't be
but things should be mostly sensible.


Usage
-----

Start this SHET client by running client.py with an argument of a directory
containing .pom files. The directory pointed to will be monitored for any
changes to any .pom files it contains and these files will be automatically
parsed.

.pom File Format
----------------

The basic format consists of several blocks like so::

	MUSIC {
		0 => /some/action;
		34 => /some/property = 1;
		_2 => /some/action "arg!";
		^1 => /some/lights;
		_^1 => /some/music;
	}

Here, bindings are being configured for a mode called MUSIC (modes are
represented either as all-caps aliases (see mode.py) or in the form
[mode-type]:[mode], for example 1:0 is the first mode (mode 0) for the left-hand
mode button on the button panel.

Five bindings are configured:

 * The first button when pressed normally will call /some/action in shet.
 * The 3rd and 4th buttons when pressed simulatneously will set /some/property
   to 1.
 * Holding the 2nd button will call /some/action with the argument "arg!".
 * Pressing middle-switch and 1 will call /some/lights.
 * Holding middle-switch and 1 will call /some/music.


If desired, you can set up a binding where the combination of buttons pressed
will be sent to the action as its first argument as a list::

	MUSIC {
		any(0 : "james"
		   ,1 : "jonathan"
		   ,2 : "karl"
		   ,3 : "matt"
		   ,4 : "tom") => /some/action "arg2";
	}

Here if any of the keys 0-4 are pressed either on their own or in tandem,
/some/action will be called with a list containing the word associated with each
button that was pressed, then "arg2" as the 2nd argument.

This can be combined with the _ and ^ symbols to require use of the
middle-switch or holding the buttons down.
