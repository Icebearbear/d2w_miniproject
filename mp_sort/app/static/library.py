from org.transcrypt.stubs.browser import *
import random
array = None
array_str = None
def gen_random_int(number, seed):
	pass

def generate():
	global array

	number = 10
	seed = 200
	result = [1,2,3,4,5,6,7,8,9,0]
	random.seed(seed)
	random.shuffle(result)
	st = ""
	array = result
	for i in range(len(result)):
		if st == "":
			st = st + result[i] 
		else:
			st = st + "," + result[i] 

	# This line is to placed the string into the HTML
	# under div section with the id called "generate"	
	document.getElementById("generate").innerHTML = st


def sortnumber1():
	'''	This function is used in Exercise 1.
		The function is called when the sort button is clicked.
		You need to do the following:
		- get the list of numbers from the "generate" HTML id, use document.getElementById(id).innerHTML
		- create a list of integers from the string of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	for outer in range(1, len(array)):
		inner = outer
		while(inner > 0 and array[inner] < array[inner-1]):
			array[inner], array[inner-1] = array[inner-1] , array[inner]
			inner = inner -1

	array_str = array

	document.getElementById("sorted").innerHTML = array_str

def sortnumber2():
	'''	This function is used in Exercise 2.
		The function is called when the sort button is clicked.
		You need to do the following:
		- Get the numbers from a string variable "value".
		- Split the string using comma as the separator and convert them to 
			a list of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	# The following line get the value of the text input called "numbers"
	value = document.getElementsByName("numbers")[0].value
	value2 = value.split(",")
	array = list(map(int, value2))

	# Throw alert and stop if nothing in the text input
	if value == "":
		window.alert("Your textbox is empty")
		return

	for outer in range(1, len(array)):
		inner = outer
		while(inner > 0 and array[inner] < array[inner-1]):
			array[inner], array[inner-1] = array[inner-1] , array[inner]
			inner = inner -1


	array_str = array

	document.getElementById("sorted").innerHTML = array_str