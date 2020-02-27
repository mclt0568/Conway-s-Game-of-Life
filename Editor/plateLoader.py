from grid import grid

def readPlate(file):
	with open("presets\\"+file+".plt","r") as f:
		return f.readlines()

def getPlateInfo(file):
	raw = readPlate(file)
	size = [int(raw[1]),int(raw[0])]
	rawPlate = raw[2:]
	plate = grid(size[0],size[1])
	coords = [0,0]
	for rawRow in rawPlate:
		for col in rawRow.strip():
			if col =="#":
				plate.setValue(coords[0],coords[1],True)
			coords[0] += 1
		coords[1] += 1
		coords[0] = 0
	return plate