import os,json
def checkCfg():
	cfg="""{
	"plate":"",
	"timeinterval":0.3,
	"autoupdate":true
}"""
	if not os.path.isfile("config.json"):
		with open("config.json","w+") as f:
			f.write(cfg)
def checkPlate():
	if not os.path.isdir("presets"):
		os.mkdir("presets")

def init():
	checkPlate()
	checkCfg()
