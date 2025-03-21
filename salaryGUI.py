"""
Chapter 9 example 
Program: salaryGUI.py
3/19/2025

**NOTE: the module breezypythongui.py MUST be in the same directory as this file for the app to run properly!

GUI based version of the weekly salary calculator from previous chapters
"""

from breezypythongui import EasyFrame
from tkinter.font import Font
# Other imports can go here

# Class Header (class name will change from project to project)
class SalaryCalc(EasyFrame):

	# Definition of our classes' constructor method
	def __init__(self):
		
		# Call to the EasyFrame class constructor
		EasyFrame.__init__(self, title = "Salary Calculator", width = 240, height = 160, resizable = False, background = "lightgreen")

		# Other components are added here
		self.addLabel(text = "Hourly Wage:", row = 0, column = 0)
		self.wageField = self.addFloatField(value = 0.0, row = 0, column = 1)
		self.addLabel(text = "No. of Hours Worked:", row = 1, column = 0)
		self.hoursField = self.addFloatField(value = 0.0, row = 0, column = 1)
		self.button = self.addButton(text = "Calculate!", row = 2, column = 0, columnspan = 2, command = self.calculate)
		self.addLabel(text = "The employee's weekly salary is:", row = 3, column = 0)
		self.result = self.addFloatField(value = 0.0, row = 3, column = 1, precision = 2, state = "readonly")

	#The event handling method for the button
	def calculate(self):
		wage = self.wageField.getNumber()
		hours = self.hoursField.getNumber()
		weeklyPay = wage * hours
		self.result.setNumber(weeklyPay)
# End of class block	

# Global definition of the main() function
def main():
	# Instantiate an object from the class into mainloop()
	SalaryCalc().mainloop()

# Global call to main() for program entry
if __name__ == '__main__':
	main()
