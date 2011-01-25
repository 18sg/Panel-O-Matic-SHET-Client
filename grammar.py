#!/usr/bin/python

from pyparsing import *

toInt = (lambda s,l,t: int(t[0]))
isStr = (lambda targ: (lambda s,l,t: t[0] == targ))

string = QuotedString("\'") | QuotedString("\"")

# SHET Paths/Args
shet_url = Word("/", alphanums+"_/" )

shet_arg = string

shet_action = shet_url("url") + Group(ZeroOrMore(shet_arg))("args")



# Modifier prefixes
hold = Optional("_")#.setParseAction(isStr("_"))

middle_switch = Optional("^")#.setParseAction(isStr("^"))


# Buttons
button_literal = Word(srange("[0-9]"), exact = 1).setParseAction(toInt)

button_chord = Group(button_literal + OneOrMore(button_literal))

button_grouping_type = Literal("any") | Literal("one")

button_names = button_literal("button") + Suppress(":") + Optional(string)("name")

button_grouping = (button_grouping_type("type")
                   + nestedExpr("(", ")",
                                delimitedList(Group(button_names)))("elements"))

buttons = button_chord("chord") | button_literal("literal") | button_grouping("grouping")



# Binding
binding = (hold("hold") + middle_switch("middle_switch")
           + buttons("buttons")
           + Suppress("=>")
           + shet_action("action")
           + Suppress(";"))



# Mode Blocks
mode_alias = Word(srange("[A-Z_]"))

mode_literal = Group(Word(srange("[0-9]"))("type")
                     + Literal(":").suppress()
                     + Word(srange("[0-9]"))("mode"))

mode = mode_alias("alias") | mode_literal("literal")


mode_block = (mode("mode")
              + nestedExpr("{", "}", OneOrMore(Group(binding)))("bindings"))



grammar = OneOrMore(Group(mode_block)).ignore(cStyleComment)


