import json

def getConfig():
	with open("config.json","r") as f:
		return json.load(f)

def writeConfig(configname,value):
	config = getConfig()
	config[configname] = value
	with open("config.json","w+") as f:
		f.write(json.dumps(config))