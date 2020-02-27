def getInfo(plate):
	raw = ""
	plateList = plate.plate
	for rows in plateList:
		for element in rows:
			if element == plate.zero:
				raw += "."
			else:
				raw+= "#"
		raw += "\n"
	raw = raw.strip()
	return [plate.cols,plate.rows,raw]
def write(name,plate):
	raw = getInfo(plate)
	with open("presets\\"+name+".plt","w+") as f:
		f.write(str(raw[0])+"\n")
		f.write(str(raw[1])+"\n")
		f.write(raw[2])