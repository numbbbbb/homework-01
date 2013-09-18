#!/usr/bin/python

import random

inputfile = open("number", "w")
for i in range(0, 10):
	inputfile.write(str(random.randint(-100, 100)) + '\n')
inputfile.close()