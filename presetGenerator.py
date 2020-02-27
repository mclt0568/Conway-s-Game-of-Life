import init,os
init.checkPlate()
x = int(input("Cols?"))
y = int(input("Rows?"))
name = input("Name?")

if os.path.isfile("presets\\"+name+".plt"):
	if not(input("presets\\"+name+".plt is already being saved, replact it?(y/n)").stirp() in ('y','Y')):
		input("Generating Cancelled. Press [Enter] to Exit")
		exit()

row = ""
data = "{}\n{}\n".format(x,y)
for i in range(x):
	row += "."
row += "\n"
for i in range(y):
	data += row

with open("presets\\"+name+".plt","w") as f:
	f.write(data)

input("Done Generating. Press [Enter] to Exit")