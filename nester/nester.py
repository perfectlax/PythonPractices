"""The nester.py module provides a function called print_lol
which prints lists that may have nested lists"""
import sys

def print_lol(the_list, indent = False,level = 0, out_put = sys.stdout):
	"""This function takes a positional argument called "the_list", which is
	any Python list (of, possibly, nested lists). Each data item in the
	provided list is (recursively) printed on its own line.
	It has a level argument to indent the nested lists, this can be turned
	on or off"""
	for each_item in the_list:
		if isinstance(each_item, list):
			print_lol(each_item, indent, level + 1, out_put)
		else:
			if indent:
				for tab_stop in range (level):
					print("\t", end = '', file = out_put)
			print(each_item, file = out_put)
