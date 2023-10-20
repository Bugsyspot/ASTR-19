#Prompt 3 defines a function and an x-value that executes if the answer is larger than some integer

import numpy as np

x = 9

#This defines what the function is
def f(x):
	return x**3 + 8

#This prints the result of f(9
def main():
	print(f"f({x}) = {f(x)}")

#This executes the program if larger than 27 and prints a message
if f(x) > 27:
	print("value was larger than 27")

#This is a fail safe for if this is imported as a module
if __name__=="__main__":
	main()
