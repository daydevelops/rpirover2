import serial

class MotorController(object):
	def __init__(self):
		self.ser = serial.Serial("/dev/ttyACM1",9600)

	def stop(self):
		self.ser.write(str.encode("S;"))

	def leftM(self, speed):
		self.ser.write(str.encode("L"+str(speed)+";"))

	def rightM(self, speed):
		self.ser.write(str.encode("R"+str(speed)+";"))

	def yawCam(self, angle):
		self.ser.write(str.encode("Y"+str(angle)+";"))
