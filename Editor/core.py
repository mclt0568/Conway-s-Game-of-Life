import time,os
from grid import grid
from termio import getControl
def run(plate,speed,auto):
	main = plate
	x = plate.cols
	y = plate.rows
	while True:
		print(main.generate())
		second = grid(x,y,zero=". ",one="# ")
		#iter grid
		coords = [0,0]
		for row in main.plate:
			for element in row:
				state = main.getValue(coords[0],coords[1])
				count = main.countNearby(coords[0],coords[1])
				if state == main.zero:
					if count == 3:
						second.setValue(coords[0],coords[1],True)
				elif state == main.one:
					if count < 2:
						second.setValue(coords[0],coords[1],False)
					elif count in (2,3):
						second.setValue(coords[0],coords[1],True)
					elif count > 3:
						second.setValue(coords[0],coords[1],False)
				coords[0]+=1
			coords[0] = 0
			coords[1] += 1
		main.updatePlate(second)
		del second
		if auto:
			time.sleep(speed)
		else:
			input("Press [Enter] to update")
		os.system("cls")