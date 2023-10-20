#Prompt 4 declares a class describing my favorite animal

class Turtle:
	#data members
	def __init__(self, arm_length, leg_length, eyes, tail, furry):
		self.arm_length = arm_length
		self.leg_length = arm_length
		self.eyes = eyes
		self.tail = tail
		self.furry = furry

	def physical_parameters(self):
		print("My favorite animal is a turtle \nand these are its physical parameters")
		print(f"Arm length = ")