from termio import setCursor,getControl,printonly,getfiles
from grid import grid
from plateWritter import write
import os
class Editor():
	def __init__(self,plate,filename):
		self.plate = plate
		self.filename = filename
		self.coords = [0,0]
	def showMenu(self):
		os.system("cls")
		item=["Back to Editor","Save","Save As","Back to Menu"]
		print("|===File Menu===|")
		print()
		for i in item:
			print("  - "+i)
		for i in range(self.plate.cols*2):
			printonly(" ")
		print("\n|===============|")
		index = 0
		setCursor(0,2);printonly(">");setCursor(0,2)
		while True:
			control = getControl()
			if control == "Down":
				if index < len(item)-1:
					index+=1
					setCursor(0,1+index);printonly(" ");setCursor(0,2+index);printonly(">");setCursor(0, 2+index)
			if control == "Up":
				if index > 0:
					index -=1
					setCursor(0,3+index);printonly(" ");setCursor(0,2+index);printonly(">");setCursor(0,2+index)
			if control == "Tog":
				print("\n\n\n")
				return item[index]
	def moveCursor(self,control):
		if control == "Up":
			if self.coords[1] > 0:
				self.coords[1] -= 1
				setCursor(self.coords[0]*2,self.coords[1]+2)
		elif control == "Down":
			if self.coords[1] < self.plate.rows-1:
				self.coords[1] += 1
				setCursor(self.coords[0]*2,self.coords[1]+2)
		elif control == "Left":
			if self.coords[0] >0:
				self.coords[0] -=1
				setCursor(self.coords[0]*2,self.coords[1]+2)
		elif control == "Right":
			if self.coords[0] < self.plate.cols-1:
				self.coords[0] += 1
				setCursor(self.coords[0]*2,self.coords[1]+2)
	def toggleTile(self):
		self.plate.setValue(self.coords[0],self.coords[1],not ((self.plate.getValue(self.coords[0],self.coords[1])) == self.plate.one))
		setCursor(0,2)
		print(self.plate.generate())
		setCursor(self.coords[0]*2,self.coords[1]+2)
	def reDraw(self):
		os.system("cls")
		print("[Ctrl][S] to save. [Ctrl][F] for menu.\n")
		print(self.plate.generate())
		setCursor(self.coords[0]*2,self.coords[1]+2)
	def savefile(self):
		write(self.filename,self.plate)
	def saveas(self):
		os.system("cls")
		print("""|====Save As====|

Name = 


|===============|""")
		setCursor(7,2)
		while True:
			name = input()
			illegal = False
			for i in ("\\","/",":","*","?","<",">","|",'"'):
				if i in name:
					illegal = True
			if name.strip() == "":
				setCursor(0,3)
				for i in range(len("File name already taken, Press [Y] to replace, [N] to make changes")):
					printonly(" ")
				setCursor(0,3)
				printonly("File name cannot be empty")
				setCursor(7,2)
			elif illegal:
				setCursor(0,3)
				for i in range(len("File name already taken, Press [Y] to replace, [N] to make changes")):
					printonly(" ")
				setCursor(0,3)
				printonly("File name contains illegal charactors")
				setCursor(7,2)
				for i in range(len(name)):
					printonly(" ")
				setCursor(7,2)
			elif os.path.isfile("presets\\"+name+".plt"):
				setCursor(0,3)
				for i in range(len("File name already taken, Press [Y] to replace, [N] to make changes")):
					printonly(" ")
				setCursor(0,3)
				printonly("File name already taken, Press [Y] to replace, [N] to make changes")
				replace = getControl()
				if replace == "Y":
					break
				else:
					setCursor(7,2)
					for i in range(len(name)):
						printonly(" ")
					setCursor(7,2)
			else:
				break
		self.filename = name
		write(self.filename,self.plate)
	def editor(self):
		os.system("cls")
		print("[Ctrl][S] to save. [Ctrl][F] for menu.\n")
		print(self.plate.generate())
		setCursor(0,2)
		while True:
			control = getControl()
			if control in ("Up","Down","Left","Right"): self.moveCursor(control)
			if control == "Menu":
				option = self.showMenu()
				if option == "Save":
					self.savefile()
				if option == "Save As":
					self.saveas()
				if option == "Back to Menu":
					break
				self.reDraw()
			if control == "Save":
				self.savefile()
			if control == "Tog": self.toggleTile()