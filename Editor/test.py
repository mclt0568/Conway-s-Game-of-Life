import ctypes,msvcrt,os
from ctypes import c_long, c_wchar_p, c_ulong, c_void_p
from os import walk
#controls:
#up down left right
#space = toggle tile
#ctrl_s = save
#ctrl_f = menu

#https://stackoverflow.com/questions/27612545/how-to-change-the-location-of-the-pointer-in-python
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

print("dejwoijdiowejdoiwjeoidjweoijdoiwjedoiwejoidjwoiedjwoiejdoiwjedoiwjedodwqswqsqwqwsqwsqiwjeoidjwoeidjwoiejdoijedoewijdoiwje")
input()
setCursor(0,1)
input()