from init import init
from config import getConfig
from grid import grid
from plateLoader import getPlateInfo
from core import run
import os
init()
config = getConfig()
if config["plate"] == "":
	input("Preset is empty. Use PresetGenerator.exe to generate a preset. Press [Enter] to Exit")
	exit()
if not os.path.isfile("presets\\"+config["plate"]+".plt"):
	input("Preset not found. Please check config.json. Press [Enter] to Exit")
	exit()
plate = getPlateInfo(config["plate"])
run(plate,config["timeinterval"],config["autoupdate"])