import os,plateLoader,core
from termio import setCursor,getControl,printonly,getfiles
from grid import grid
from editor import Editor
from init import init
from config import getConfig,writeConfig
#controls:
#up down left right
#space = toggle tile
#ctrl_s = save
#ctrl_f = menu
#Y/N = Yes/No
config = getConfig()
def mainMenu():
	os.system("cls")
	item=["New File","Load File","Start Simulate","Help"]
	print("|================Welcome to Frank's plt editor====================|")
	print("|=Please use [↑][↓] option from below, press [Space] to enter.==|")
	print()
	for i in item:
		print("  - "+i)
	index = 0
	setCursor(0,3);printonly(">");setCursor(0,3)
	while True:
		control = getControl()
		if control == "Down":
			if index < len(item)-1:
				index+=1
				setCursor(0,2+index);printonly(" ");setCursor(0,3+index);printonly(">");setCursor(0,3+index)
		if control == "Up":
			if index > 0:
				index -=1
				setCursor(0,4+index);printonly(" ");setCursor(0,3+index);printonly(">");setCursor(0,3+index)
		if control == "Tog":
			print("\n\n\n")
			return item[index]

def helpMenu():
	os.system("cls")
	print("|============================Help Menu============================|")
	print("|===============Press [Space] to exit when finished===============|")
	print("")
	print("Select New File to create a file, or Load file to load an existed")
	while True:
		control = getControl()
		if control == "Tog":
			return None

def newFileSelector():
	os.system("cls")
	print("|=====Select a size for this file=====|")
	print()
	print("Colums = ")
	print("Rows = ")
	print("Name of the preset = ")
	while True:
		setCursor(9,2)
		cols = input()
		try:
			cols = int(cols)
			if cols < 1:
				raise TypeError
			break
		except Exception:
			setCursor(0,6)
			print("Columns needs to be a valid NUMBER.")
			setCursor(9,2)
			for i in range(len(cols)):
				printonly(" ")

	setCursor(0,6)
	for i in range(len("Columns needs to be a valid NUMBER.")):
		printonly(" ")

	while True:
		setCursor(7,3)
		rows = input()
		try:
			rows = int(rows)
			if rows < 1:
				raise TypeError
			break
		except Exception:
			setCursor(0,6)
			print("Rows needs to be a valid NUMBER.")
			setCursor(7,3)
			for i in range(len(rows)):
				printonly(" ")

	setCursor(0,6)
	for i in range(len("Rows needs to be a valid NUMBER.")):
		printonly(" ")

	while True:
		setCursor(21,4)
		name = input()
		illegal = False
		for i in ("\\","/",":","*","?","<",">","|",'"'):
			if i in name:
				illegal = True
		if name.strip() == "":
			setCursor(0,6)
			for i in range(len("File name already taken, Press [Y] to replace, [N] to make changes")):
				printonly(" ")
			setCursor(0,6)
			printonly("File name cannot be empty")
			setCursor(21,4)
		elif illegal:
			setCursor(0,6)
			for i in range(len("File name already taken, Press [Y] to replace, [N] to make changes")):
				printonly(" ")
			setCursor(0,6)
			printonly("File name contains illegal charactors")
			setCursor(21,4)
			for i in range(len(name)):
				printonly(" ")
		elif os.path.isfile("presets\\"+name+".plt"):
			setCursor(0,6)
			for i in range(len("File name already taken, Press [Y] to replace, [N] to make changes")):
				printonly(" ")
			setCursor(0,6)
			printonly("File name already taken, Press [Y] to replace, [N] to make changes")
			replace = getControl()
			if replace == "Y":
				break
			else:
				setCursor(0,6)
				for i in range(len(name)):
					printonly(" ")
		else:
			break

	return [grid(cols,rows,zero = ". ",one="# "),name]

def fileSelector():
	os.system("cls")
	item=getfiles()
	print("|================Welcome to Frank's plt editor====================|")
	print("|=Please use [↑][↓] option from below, press [Space] to enter.==|")
	print()
	for i in item:
		print("  - "+i)
	index = 0
	setCursor(0,3);printonly(">");setCursor(0,3)
	while True:
		control = getControl()
		if control == "Down":
			if index < len(item)-1:
				index+=1
				setCursor(0,2+index);printonly(" ");setCursor(0,3+index);printonly(">");setCursor(0,3+index)
		if control == "Up":
			if index > 0:
				index -=1
				setCursor(0,4+index);printonly(" ");setCursor(0,3+index);printonly(">");setCursor(0,3+index)
		if control == "Tog":
			print("\n\n\n")
			return item[index]

while True:
	init()
	option = mainMenu()
	if option == "Help":
		helpMenu()
	elif option == "New File":
		fileInfo = newFileSelector()
		edit = Editor(fileInfo[0],fileInfo[1])
		edit.editor()
	elif option == "Load File":
		filename = fileSelector()[:-4]
		fileInfo = [plateLoader.getPlateInfo(filename),filename]
		edit = Editor(fileInfo[0],fileInfo[1])
		edit.editor()
	elif option	== "Start Simulate":
		filename = fileSelector()[:-4]
		plate = plateLoader.getPlateInfo(filename)
		core.run(plate,config["timeinterval"],True)