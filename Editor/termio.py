import ctypes,msvcrt,os
from ctypes import c_long, c_wchar_p, c_ulong, c_void_p
from os import walk
gHandle = ctypes.windll.kernel32.GetStdHandle(c_long(-11))
def setCursor(x,y):
	value = x + (y << 16)
	ctypes.windll.kernel32.SetConsoleCursorPosition(gHandle, c_ulong(value))
def printonly(string):
	ctypes.windll.kernel32.WriteConsoleW(gHandle, c_wchar_p(string), c_ulong(len(string)), c_void_p(), None)
#https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
def getfiles():
	f = []
	for (dirpath, dirnames, filenames) in walk("presets\\"):
		f.extend(filenames)
	return f
#learned from getpass module (windows)
def getControl():
	rawControl = msvcrt.getwch()
	if rawControl in ("à","\x00"):
		secondary = msvcrt.getwch()
		if secondary == "H":
			control = "Up"
		elif secondary == "M":
			control = "Right"
		elif secondary == "P":
			control = "Down"
		elif secondary == "K":
			control = "Left"
		return control
	elif rawControl in (" ","\r"):
		return "Tog"
	elif rawControl == "\x13":
		return "Save"
	elif rawControl == "\x06":
		return "Menu"
	elif rawControl in ("y","Y"):
		return "Y"
	elif rawControl in ("n","N"):
		return "N"
	else:
		return "Invalid"
