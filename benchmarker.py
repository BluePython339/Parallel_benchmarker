# Made by the one and only Bluepython339
# python 3.8.3

from subprocess import *
import timeit
import os
import matplotlib.pyplot as plt
import argparse


parser = argparse.ArgumentParser(description='C and C++ executable benchmarker.')
parser.add_argument('-e','--executable', help="executable you want to benchmark", type=str, required=True)
parser.add_argument('-i','--Max_Input_Size', help="maximum input you want to benchmark (default: 10000000)", type=int, default=10000000)
parser.add_argument('-c','--competitor', help="competitor executable to compare benchmark", type=str)


def execute(datasize, executable):
	print("checking datasize {}".format(datasize))
	procces = call(['./{} {}'.format(executable, datasize)],shell=True) #start the c script with passed data

def bench_it(maxInput, executable):
	output_num = [] #list of inputs we tried
	output_time = [] # list of times it look per input
	inputsize = 100000 # starting input size
	 #i mad it easy for you to configure
	while inputsize < maxInput: #
		print("now trying: {}".format(inputsize))
		#creating the timeing object
		t = timeit.Timer("execute({},'{}')".format(inputsize, executable), setup="from __main__ import execute")
		#adding the new datasize to the list
		output_num.append(inputsize)
		#starting the timing sequence
		output_time.append(t.timeit(1))
		#calculating the new input size and rounding it to the nearest int
		inputsize = int(inputsize+(inputsize/4))

	return output_num, output_time #returning the test results

if __name__ == "__main__":
	args = parser.parse_args()

	a = bench_it(args.Max_Input_Size, args.executable)
	plt.plot(a[0],a[1], label=args.executable)
	if args.competitor:
		b = bench_it(args.Max_Input_Size, args.competitor)
		plt.plot(b[0],b[1], label=args.competitor) #calculating the plot values
		plt.title("{} benchmark compared to {}".format(args.executable, args.competitor))
	else:
		plt.title("benchmark for {}")
	plt.xlabel("inputsize")
	plt.ylabel("time in seconds")
	plt.legend()
	plt.show() #plotting the graph