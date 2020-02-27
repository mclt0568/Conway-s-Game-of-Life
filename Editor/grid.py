class grid:
	def __init__(self,rows:int,cols:int,zero=". ",one="# "):
		self.rows = rows
		self.cols = cols
		self.zero = zero
		self.one = one
		rowPlate = []
		for i in range(cols):
			rowPlate.append(zero)
		self.plate = []
		for i in range(rows):
			self.plate.append(rowPlate.copy())
	def generate(self):
		zero = self.zero
		one = self.one
		gridPloted = ""
		for i in self.plate:
			for j in i:
				gridPloted += j
			gridPloted += "\n"
		return gridPloted
	def getValue(self,x,y):
		return self.plate[y][x]
	def setValue(self,x,y,value:bool):
		if value:
			self.plate[y][x] = self.one
		else:
			self.plate[y][x] = self.zero
	def setAll(self,value:bool):
		rowPlate = []
		plate = []
		if value:
			bit = self.one
		else:
			bit = self.zero
		for i in range(self.cols):
			rowPlate.append(bit)
		for i in range(self.rows):
			plate.append(rowPlate.copy())
		self.plate = plate.copy()
	def getBorderState(self,x,y):
		state = 0b10000 #digits: 1 Top Bottom Left Right
		if y == 0:
			state = state | 0b11000
		elif y == self.rows-1:
			state = state | 0b0100
		if x == 0:
			state = state | 0b10010
		elif x==self.rows-1:
			state = state | 0b10001
		return int("0b"+bin(state)[3:],2)
	def getNearby(self,x,y):
		state = self.getBorderState(x,y)
		Nearby=[]
		temp = []
		if state == 0:
			coords = [[-1,-1],[0,-1],[1,-1],[-1,0],[1,0],[-1,1],[0,1],[1,1]]
		elif state == 10:
			coords=[[1,0],[0,1],[1,1]]
		elif state == 8:
			coords=[[-1,0],[1,0],[-1,1],[0,1],[1,1]]
		elif state == 9:
			coords=[[-1,0],[-1,1],[0,1]]
		elif state == 2:
			coords=[[0,-1],[1,-1],[1,0],[1,1],[0,1]]
		elif state == 1:
			coords=[[-1,-1],[0,-1],[-1,0],[-1,1],[0,1]]
		elif state == 6:
			coords=[[0,-1],[1,-1],[1,0]]
		elif state == 4:
			coords=[[-1,-1],[0,-1],[1,-1],[1,0],[1,0]]
		elif state == 5:
			coords=[[-1,-1],[0,-1],[-1,0]]
		for i in coords:
			temp.append(self.getValue(x+i[0],y+i[1]))
		for i in temp:
			if i == self.one:
				Nearby.append(True)
			else:
				Nearby.append(False)
		return Nearby
	def countNearby(self,x,y):
		Nearby = self.getNearby(x,y)
		count = 0
		for i in Nearby:
			if i:count+=1
		return count
	def updatePlate(self,grid):
		if grid.cols != self.cols:
			raise TypeError("Grid not same size:Cols")
		if grid.rows != self.rows:
			raise TypeError("Grid not same size:Rows")
		self.plate = grid.plate