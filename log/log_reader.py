import sys

class LogParameters(dict):
	def __init__(self, time, rpm, mph, throttle, load, fuelStatus):
		dict.__init__({})
		self['time'] = time
		self['rpm'] = rpm
		self['mph'] = mph
		self['throttle'] = throttle
		self['load'] = load
		self['fuelStatus'] = fuelStatus

	def __str__(self):
		return ("Time: " + str(self['time']) + ", RPM: " + str(self['rpm']) + ", MHP: " + str(self['mph']) + ", Throttle: " + str(self['throttle']) + ", Load: " + str(self['load']) + ", Fuel Status: " + str(self['fuelStatus']))


class LogReader:
	def __init__(self, archive):
		self.readLog(archive)
	
	def readLog(self, archive):
		self.logList = []
		try:
			with open(archive) as arc:
				text = arc.readlines()
			
			text.pop(0)
			i = 0
			for eachLine in text:
				if not i % 60:				
					parametersList = eachLine.strip().split(',')
					self.logList.append(LogParameters(parametersList[0], \
								  	  parametersList[1], \
								  	  parametersList[2], \
								  	  parametersList[3], \
								  	  parametersList[4], \
								  	  parametersList[5]))
				i+=1

		except IOError as ioerr:
			print("\nIOerr: " + str(ioerr))	

	def __str__(self):
		string = ""
		return string.join([(str(x) + '\n') for x in self.logList])
	
if __name__ == "__main__":
	reader = LogReader(sys.argv[1])
	print(str(reader))
	
				
	

